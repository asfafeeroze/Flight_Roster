import React, { useState } from 'react';
import './CreateAccount.css'; // Make sure you have the corresponding CSS file

const CreateAccount = () => {
  const [email, setEmail] = useState('');
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [dob, setDob] = useState('');
  const [gender, setGender] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    // Here you would handle creating an account
    console.log(email, username, password, confirmPassword, dob, gender);
    // You should also implement validation and password confirmation checks
  };

  return (
    <div className="create-account-page">
      <h2>Create an Account</h2>
      <form onSubmit={handleSubmit} className="create-account-form">
        <div className="form-group">
          <input
            type="email"
            placeholder="Enter your email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
          <input
            type="text"
            placeholder="Create a Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        <div className="form-group">
          <input
            type="text"
            placeholder="Enter your username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
          <input
            type="password"
            placeholder="Confirm your Password"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
            required
          />
        </div>
        <div className="form-group">
          <input
            type="date"
            placeholder="Enter your date of birth"
            value={dob}
            onChange={(e) => setDob(e.target.value)}
            required
          />
          <input
            type="text"
            placeholder="Enter your Gender"
            value={gender}
            onChange={(e) => setGender(e.target.value)}
          />
        </div>
        <button type="submit" className="create-account-button">Create an account!</button>
        <a href="/" className="login-link">Go back to Log in</a>
      </form>
    </div>
  );
};

export default CreateAccount;
