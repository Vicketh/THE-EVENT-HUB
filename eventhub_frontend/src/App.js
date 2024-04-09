import React, { useState, useEffect, useRef } from 'react';
import { BiSolidHome } from "react-icons/bi";
import { MdWavingHand } from "react-icons/md";
import { BsFillBellFill } from "react-icons/bs";
import { BiSearchAlt } from "react-icons/bi";
import { MdOutlineLogin } from "react-icons/md";
import { MdLogout } from "react-icons/md";
import { FaBars, FaMapPin } from "react-icons/fa";
import { MdGroups } from "react-icons/md";
import { MdCategory } from "react-icons/md";
import { IoLogoWechat } from "react-icons/io5";
import './App.css';

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

    document.addEventListener("mousedown", handler);

    return () => {
      document.removeEventListener("mousedown", handler);
    }
  }, []);

  const handleLogout = () => {
    localStorage.removeItem('user');
    setUser(null);
  };

  return (
    <div className="App">
      <div className="dashboard">
        <div className="header">
          <div className="logo">
            <img src="logo.png" alt="Event-Hub Logo" />
            <h1>The Event-Hub</h1>
          </div>
          <div className="user-info">
            {user ? (
              <>
                <span className="greeting">Hi, {user.username} <MdWavingHand/></span>
                <div className="notification">
                  <span>Notifications <BsFillBellFill/></span>
                </div>
                <div className="search-bar">
                  <input type="text" placeholder="Search" />
                  <BiSearchAlt className="search-icon" />
                </div>
                <div className="logout" onClick={handleLogout}>
                  <span>Logout <MdLogout/></span>
                </div>
              </>
            ) : (
              <button>Login <MdOutlineLogin/></button>
            )}
          </div>
        </div>
        <div className="menu-container" ref={menuRef}>
          <div className="menu-trigger" onClick={() => setOpen(!open)}>
            <div className={`dropdown-menu ${open ? "active" : "inactive"}`}>
              <h3>Menu <FaBars/> <br /><span>The Event-Hub <FaMapPin/></span></h3>
              <ul>
                <DropdownItem icon={<BiSolidHome/>} text="Home" />
                <DropdownItem icon={<MdGroups/>} text="My Events" />
                <DropdownItem icon={<MdCategory/>} text="Categories" />
                <DropdownItem icon={<IoLogoWechat/>} text="Chats" />
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

function DropdownItem(props) {
  return (
    <li>{props.icon} {props.text}</li>
  );
}

export default App;
