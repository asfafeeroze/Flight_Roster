import mongoose from 'mongoose';

const PilotSchema = new mongoose.Schema({
  name: { type: String, required: true },
  age: { type: Number, required: true },
  gender: { type: String, required: true },
  nationality: { type: String, required: true },
  known_languages: { type: [String], required: true },
  vehicle_restriction: { type: String, required: true },
  allowed_range: { type: Number, required: true },
  seniority_level: { type: String, enum: ['senior', 'junior', 'trainee'], required: true }
});

const Pilot = mongoose.model('Pilot', PilotSchema);
export default Pilot;
