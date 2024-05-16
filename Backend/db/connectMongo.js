import mongoose from 'mongoose';
import dotenv from 'dotenv';

dotenv.config();

const ConnectMongo = async () => {
  try {
    await mongoose.connect(process.env.MONGO, {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    });
    console.log('MongoDB successfully connected');
  } catch (err) {
    console.error('MongoDB connection error:', err);
    process.exit(1);
  }
};

export default ConnectMongo;
