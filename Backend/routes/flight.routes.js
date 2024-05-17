import express from 'express';
import db from '../db/mySql.js';  // Assuming db.js is in the same directory

const router = express.Router();

// POST route to create a new flight
router.post('/flights', async (req, res) => {
  const { flightNumber, date, duration, distance, source_id, destination_id, vehicle_type_id, shared_flight_info_id } = req.body;
  try {
    const [result] = await db.query(
      `INSERT INTO flights (flight_number, date, duration, distance, source_id, destination_id, vehicle_type_id, shared_flight_info_id) 
       VALUES (?, ?, ?, ?, ?, ?, ?, ?)`,
      [flightNumber, date, duration, distance, source_id, destination_id, vehicle_type_id, shared_flight_info_id]
    );
    res.status(201).send({ id: result.insertId, ...req.body });
  } catch (error) {
    res.status(400).send(error.message);
  }
});

// GET route to retrieve all flights
router.get('/flights', async (req, res) => {
  try {
    const [flights] = await db.query(`SELECT * FROM flights`);
    res.status(200).send(flights);
  } catch (error) {
    res.status(500).send(error.message);
  }
});

// GET route to retrieve a single flight by flightNumber
router.get('/flights/:flightNumber', async (req, res) => {
  try {
    const [flights] = await db.query(`SELECT * FROM flights WHERE flight_number = ?`, [req.params.flightNumber]);
    if (flights.length === 0) {
      return res.status(404).send();
    }
    res.send(flights[0]);
  } catch (error) {
    res.status(500).send(error.message);
  }
});

// PATCH route to update a flight by flightNumber
router.patch('/flights/:flightNumber', async (req, res) => {
  const updates = req.body;
  try {
    const keys = Object.keys(updates);
    const values = keys.map(key => updates[key]);

    const setString = keys.map(key => `${key} = ?`).join(', ');
    values.push(req.params.flightNumber);

    const [result] = await db.query(`UPDATE flights SET ${setString} WHERE flight_number = ?`, values);
    if (result.affectedRows === 0) {
      return res.status(404).send();
    }
    res.send({ ...updates });
  } catch (error) {
    res.status(400).send(error.message);
  }
});

// DELETE route to delete a flight by flightNumber
router.delete('/flights/:flightNumber', async (req, res) => {
  try {
    const [result] = await db.query(`DELETE FROM flights WHERE flight_number = ?`, [req.params.flightNumber]);
    if (result.affectedRows === 0) {
      return res.status(404).send();
    }
    res.send({ message: 'Flight deleted successfully.' });
  } catch (error) {
    res.status(500).send(error.message);
  }
});

export default router;
