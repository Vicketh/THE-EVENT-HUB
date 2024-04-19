import React, { useState, useEffect, useRef } from 'react';
import { BiSolidHome } from 'react-icons/bi';
import { FaBars, FaMapPin } from 'react-icons/fa';
import { MdGroups } from 'react-icons/md';
import { MdCategory } from 'react-icons/md';
import { IoLogoWechat } from 'react-icons/io5';
import './App.css';
import Header from './components/Header';

function App() {
  const [user, setUser] = useState(null);
  const [open, setOpen] = useState(false);

  let menuRef = useRef();

  useEffect(() => {
    const loggedInUser = localStorage.getItem('user');
    if (loggedInUser) {
      setUser(JSON.parse(loggedInUser));
    }

    let handler = (e) => {
      if (!menuRef.current.contains(e.target)) {
        setOpen(false);
      }
    };

    document.addEventListener('mousedown', handler);

    return () => {
      document.removeEventListener('mousedown', handler);
    };
  }, []);

  const handleLogout = () => {
    localStorage.removeItem('user');
    setUser(null);
  };

  return (
    <div className='App'>
      <div className='dashboard'>
        <Header user={user} setUser={setUser} handleLogout={handleLogout} />
        <div className='menu-container' ref={menuRef}>
          <div className='menu-trigger' onClick={() => setOpen(!open)}>
            <div className={`dropdown-menu ${open ? 'active' : 'inactive'}`}>
              <h3>
                Menu <FaBars /> <br />
                <span>
                  The Event-Hub <FaMapPin />
                </span>
              </h3>
              <ul>
                <DropdownItem icon={<BiSolidHome />} text='Home' />
                <DropdownItem icon={<MdGroups />} text='My Events' />
                <DropdownItem icon={<MdCategory />} text='Categories' />
                <DropdownItem icon={<IoLogoWechat />} text='Chats' />
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

function DropdownItem({ icon, text }) {
  return (
    <li>
      {icon} {text}
    </li>
  );
}

export default App;
