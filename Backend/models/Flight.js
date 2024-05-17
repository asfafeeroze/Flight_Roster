import { Sequelize, Model, DataTypes } from 'sequelize';
import sequelize from '../db/sequelize.js';  // Importing the configured Sequelize instance

class Flight extends Model {}

Flight.init({
  flight_number: {
    type: DataTypes.STRING(10),
    allowNull: false,
    primaryKey: true,
    unique: true,
    validate: {
      notNull: { msg: "Flight number must be provided" },
      notEmpty: { msg: "Flight number must not be empty" }
    }
  },
  date: {
    type: DataTypes.DATE,
    allowNull: false,
    validate: {
      notNull: { msg: "Date must be provided" },
      isDate: { msg: "Must be a valid date" }
    }
  },
  duration: {
    type: DataTypes.INTEGER,
    allowNull: false,
    validate: {
      isInt: { msg: "Duration must be an integer" },
      min: 1,
      notNull: { msg: "Duration must be provided" }
    }
  },
  distance: {
    type: DataTypes.INTEGER,
    allowNull: false,
    validate: {
      isInt: { msg: "Distance must be an integer" },
      min: 1,
      notNull: { msg: "Distance must be provided" }
    }
  },
  source_id: {
    type: DataTypes.INTEGER,
    allowNull: false,
    validate: {
      isInt: { msg: "Source ID must be an integer" },
      notNull: { msg: "Source ID must be provided" }
    }
  },
  destination_id: {
    type: DataTypes.INTEGER,
    allowNull: false,
    validate: {
      isInt: { msg: "Destination ID must be an integer" },
      notNull: { msg: "Destination ID must be provided" }
    }
  },
  vehicle_type_id: {
    type: DataTypes.INTEGER,
    allowNull: false,
    validate: {
      isInt: { msg: "Vehicle Type ID must be an integer" },
      notNull: { msg: "Vehicle Type ID must be provided" }
    }
  },
  shared_flight_info_id: {
    type: DataTypes.INTEGER,
    allowNull: true  // Assuming this can be null if the flight is not shared
  }
}, {
  sequelize,
  modelName: 'Flight',
  tableName: 'flights',
  timestamps: false  // Assuming no need to track createdAt or updatedAt
});

export default Flight;
