import { DataTypes } from 'sequelize';
import sequelize from '../db/sequelize.js';

const Passenger = sequelize.define('Passenger', {
  PassengerID: {
    type: DataTypes.INTEGER,
    autoIncrement: true,
    primaryKey: true
  },
  PassportNumber: {
    type: DataTypes.INTEGER,
    unique: true
  },
  CustomerName: {
    type: DataTypes.STRING(100)
  },
  Seat_Assigned: {
    type: DataTypes.STRING(5)
  },
  Disabilities: {
    type: DataTypes.TEXT
  },
  Age: {
    type: DataTypes.INTEGER
  },
  FlightNumber: {
    type: DataTypes.STRING(10)
  },
  PhoneNumber: {
    type: DataTypes.STRING(20)
  },
  Gender: {
    type: DataTypes.STRING(10)
  },
  Nationality: {
    type: DataTypes.STRING(50)
  },
  SeatType: {
    type: DataTypes.STRING(10),
    allowNull: false,
    validate: {
      isIn: [['business', 'economy']]
    }
  },
  ParentInfo: {
    type: DataTypes.STRING(100),
    allowNull: true
  },
  AffiliatedPassengerIDs: {
    type: DataTypes.JSON,
    allowNull: true
  }
}, {
  tableName: 'Passenger'
});

export default Passenger;
