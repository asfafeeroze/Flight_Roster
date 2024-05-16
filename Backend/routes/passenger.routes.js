import express from 'express';
import Passenger from '../models/Passenger.js';

const router = express.Router();

// Get all passengers
router.get('/', async (req, res) => {
  try {
    const passengers = await Passenger.findAll();
    res.json(passengers);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Get a single passenger by ID
router.get('/:id', async (req, res) => {
  try {
    const passenger = await Passenger.findByPk(req.params.id);
    if (!passenger) {
      return res.status(404).json({ error: 'Passenger not found' });
    }
    res.json(passenger);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Create a new passenger
router.post('/', async (req, res) => {
  try {
    const passenger = await Passenger.create(req.body);
    res.status(201).json(passenger);
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

// Update a passenger by ID
router.put('/:id', async (req, res) => {
  try {
    const passenger = await Passenger.findByPk(req.params.id);
    if (!passenger) {
      return res.status(404).json({ error: 'Passenger not found' });
    }
    await passenger.update(req.body);
    res.json(passenger);
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

// Delete a passenger by ID
router.delete('/:id', async (req, res) => {
  try {
    const passenger = await Passenger.findByPk(req.params.id);
    if (!passenger) {
      return res.status(404).json({ error: 'Passenger not found' });
    }
    await passenger.destroy();
    res.json({ message: 'Passenger deleted' });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

export default router;
