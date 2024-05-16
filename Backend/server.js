import dotenv from 'dotenv';
import express from 'express';
import connectMongo from './db/connectMongo.js';
import sequelize from './db/sequelize.js';
import authRoutes from './routes/auth.routes.js';
import passengerRoutes from './routes/passenger.routes.js';
import flightRoutes from './routes/flight.routes.js';
import pilotRoutes from './routes/pilot.routes.js';

dotenv.config();

const app = express();
app.use(express.json());

// Connect to MongoDB
connectMongo();

// Connect to MySQL using Sequelize
sequelize.authenticate()
  .then(() => console.log('Sequelize successfully connected'))
  .catch(err => console.log('Sequelize connection error:', err));

// Routes
app.use('/api/auth', authRoutes); // Use the auth routes
app.use('/api/passengers', passengerRoutes); // Use the passenger routes
app.use('/api/flights', flightRoutes);
app.use('/api/pilots', pilotRoutes);

const port = process.env.PORT || 3000;

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
