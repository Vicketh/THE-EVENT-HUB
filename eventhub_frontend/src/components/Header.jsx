import React from 'react';
import { MdWavingHand } from 'react-icons/md';
import { BsFillBellFill } from 'react-icons/bs';
import { BiSearchAlt } from 'react-icons/bi';
import { MdOutlineLogin } from 'react-icons/md';
import { MdLogout } from 'react-icons/md';
import Logo from '../img/logo.png';

const Header = ({ user, setUser, handleLogout }) => {
  return (
    <div className='header'>
      <div className='logo'>
        <img src={Logo} alt='Event-Hub Logo' />
        <h1>The Event-Hub</h1>
      </div>
      <div className='user-info'>
        {user ? (
          <>
            <span className='greeting'>
              Hi, {user.username} <MdWavingHand />
            </span>
            <div className='notification'>
              <span>
                Notifications <BsFillBellFill />
              </span>
            </div>
            <div className='search-bar'>
              <input type='text' placeholder='Search' />
              <BiSearchAlt className='search-icon' />
            </div>
            <div className='logout' onClick={handleLogout}>
              <span>
                Logout <MdLogout />
              </span>
            </div>
          </>
        ) : (
          <button>
            Login <MdOutlineLogin />
          </button>
        )}
      </div>
    </div>
  );
};

export default Header;
