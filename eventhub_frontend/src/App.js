import React from 'react';
import './App.css';

function App() {
  const username = "Vick";

  return (
    <div className="App">
      <div className="dashboard">
        <div className="logo">
          <img src="logo.png" alt="Event-Hub Logo" />
          <h1>The Event-Hub</h1>
        </div>
        <div className="user-info">
          <span className="greeting">Hi, {username}</span>
          <div className="notification">
            <i className="fas fa-bell"></i>
            <span>Notifications</span>
            {/* Notification dropdown goes here */}
          </div>
          <div className="search-bar">
            <input type="text" placeholder="Search" />
            <i className="fas fa-search"></i>
          </div>
          <div className="logout">
            <span>Logout</span>
            <i className="fas fa-user-circle"></i>
            {/* Logout functionality goes here */}
          </div>
        </div>
        <div className="menu">
          <i className="fas fa-map-marker-alt"></i>
          <ul>
            <li>Home</li>
            <li>My Events</li>
            <li>Categories</li>
            <li>Chats</li>
          </ul>
        </div>
      </div>
      <div className="map-container">
        {/* Google Map component goes here */}
      </div>
      {/* Review boxes component goes here */}
      <div className="social-media">
        {/* Social media links */}
      </div>
      <div className="chat-now">
        <i className="fas fa-comment-alt"></i>
        {/* Chat now functionality goes here */}
      </div>
    </div>
  );
}

export default App;
