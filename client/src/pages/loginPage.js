import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import './Login.css'; // Ensure this is the path to your CSS for the login page

const LoginPage = () => {
  // State for the username and password
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  // Handler for when the form is submitted
  const handleLogin = (event) => {
    event.preventDefault();
    // Here you would handle the login logic
    console.log('Login attempt with:', username, password);
  };

  return (
    <div className="login-page">
      <h2>Login</h2>
      <form onSubmit={handleLogin} className="login-form">
        <div className="input-group">
          <label htmlFor="username">Username</label>
          <input
            id="username"
            type="text"
            placeholder="E.g: johndoe"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </div>
        <div className="input-group">
          <label htmlFor="password">Password</label>
          <input
            id="password"
            type="password"
            placeholder="Enter your password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        <button type="submit" className="login-button">Log in</button>
      </form>
      <div className="signup-link">
        New? <Link to="/create-account">Create an account!</Link>
      </div>
    </div>
  );
};

export default LoginPage;