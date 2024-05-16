import express from 'express';
import User from '../models/User.js';
import bcrypt from 'bcryptjs';
import jwt from 'jsonwebtoken';

const router = express.Router();

router.get('/check-email', async (req, res) => {
  const { email } = req.query;
  try {
      const user = await User.findOne({ email });
      if (user) {
          return res.status(200).json({ exists: true });
      } else {
          return res.status(200).json({ exists: false });
      }
  } catch (error) {
      res.status(500).send('Server error');
  }
});

router.get('/check-username', async (req, res) => {
  const { username } = req.query;
  try {
      const user = await User.findOne({ username });
      if (user) {
          return res.status(200).json({ exists: true });
      } else {
          return res.status(200).json({ exists: false });
      }
  } catch (error) {
      res.status(500).send('Server error');
  }
});

router.post('/register', async (req, res) => {
  try {
    const { username, email, password } = req.body;
    const user = new User({ username, email, password });
    await user.save();
    res.status(201).send('User created');
  } catch (error) {
    res.status(400).send(error);
  }
});

router.post('/login', async (req, res) => {
  try {
    const { email, password } = req.body;
    const user = await User.findOne({ email });
    if (!user || !(await bcrypt.compare(password, user.password))) {
      return res.status(401).send('Invalid login credentials');
    }
    const token = jwt.sign({ _id: user._id }, 'secret');
    res.send({ token });
  } catch (error) {
    res.status(500).send(error);
  }
});

router.post('/logout', (req, res) => {
  res.send('Logged out');
});

export default router;
