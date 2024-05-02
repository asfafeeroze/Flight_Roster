from pymongo import MongoClient

def connectDB():
    # Replace the connection string with your MongoDB connection string
    # You can obtain the connection string from your MongoDB Atlas dashboard or configure it locally
    # For example, if your database is running on localhost, the connection string might look like this:
    # "mongodb://localhost:27017/"

    connection_string = "mongodb+srv://asfafeeroze:1234@cluster0.zj78qtj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    client = MongoClient(connection_string)

    # Access a specific database (replace "your_database_name" with your actual database name)
    db = client.Cluster0
    print("Connection established to your db")
    return db
    # Close the connection when you're done
    # client.close()

# Function to get all collections in the database
# def retrieve_all_from_collection(db, collection_name):
#     """Retrieves all documents from the specified collection."""
#     collection = db[collection_name]
#     documents = list(collection.find())
#     return documents

# Insert functions

def insert_cabin_crew(db, cabin_crew_data):
    """Inserts a single cabin crew document into the MongoDB collection."""
    cabin_crew_collection = db.cabin_crew
    result = cabin_crew_collection.insert_one(cabin_crew_data)
    return result.inserted_id

def insert_user(db, user_data):
    """Inserts a single user document into the MongoDB collection."""
    user_collection = db.users
    result = user_collection.insert_one(user_data)
    return result.inserted_id


def insert_admin(db, admin_data):
    """Inserts a single admin document into the MongoDB collection."""
    admin_collection = db.admins
    result = admin_collection.insert_one(admin_data)
    return result.inserted_id


def insert_pilot(db, pilot_data):
    """Inserts a single pilot document into the MongoDB collection."""
    pilot_collection = db.pilots
    result = pilot_collection.insert_one(pilot_data)
    return result.inserted_id


def insert_aircraft(db, aircraft_data):
    """Inserts a single aircraft document into the MongoDB collection."""
    aircraft_collection = db.aircraft
    result = aircraft_collection.insert_one(aircraft_data)
    return result.inserted_id


def insert_passenger_info(db, passenger_info_data):
    """Inserts a single passenger information document into the MongoDB collection."""
    passenger_info_collection = db.passenger_info
    passenger_info_collection.insert_one(passenger_info_data)


def insert_flight_information(db, flight_information_data):
    """Inserts a single flight information document into the MongoDB collection."""
    flight_information_collection = db.flight_information
    result = flight_information_collection.insert_one(flight_information_data)
    return result.inserted_id


def insert_roster_entry(db, roster_entry_data):
    """Inserts a single roster entry document into the MongoDB collection."""
    roster_entry_collection = db.roster_entry
    roster_entry_collection.insert_one(roster_entry_data)


# User data insertion function


def main():
    db = connectDB()
    
    users_data = [
        {"_id": 1,"Email": "john.doe@example.com", "Password": "johndoe123"},
        {"_id": 2,"Email": "jane.smith@example.com", "Password": "janepass123"},
        {"_id": 3,"Email": "michael.jones@example.com", "Password": "mikepass456"},
        {"_id": 4,"Email": "emily.brown@example.com", "Password": "emilypass789"},
        {"_id": 5,"Email": "david.wilson@example.com", "Password": "davidpass321"},
        {"_id": 6,"Email": "sarah.miller@example.com", "Password": "sarahpass654"},
        {"_id": 7,"Email": "james.taylor@example.com", "Password": "jamespass987"},
        {"_id": 8,"Email": "laura.clark@example.com", "Password": "laurapass123"},
        {"_id": 9,"Email": "robert.white@example.com", "Password": "robertpass456"},
        {"_id": 10,"Email": "mary.hall@example.com", "Password": "marypass789"}
    ]
    for user_data in users_data:
        insert_user(db, user_data)
    

    

    aircraft_data = [
        {"_id": 1, "AircraftID": 1, "AircraftType": "Boeing 747", "Manufacturer": "Boeing", "Layout": "@layout1", "Capacity": 500, "Model": "747-400"},
        {"_id": 2, "AircraftID": 2, "AircraftType": "Airbus A320", "Manufacturer": "Airbus", "Layout": "@layout1", "Capacity": 200, "Model": "A320neo"},
        {"_id": 3, "AircraftID": 3, "AircraftType": "Boeing 777", "Manufacturer": "Boeing", "Layout": "@layout1", "Capacity": 400, "Model": "777-300ER"},
        {"_id": 4, "AircraftID": 4, "AircraftType": "Airbus A380", "Manufacturer": "Airbus", "Layout": "@layout1", "Capacity": 800, "Model": "A380-800"},
        {"_id": 5, "AircraftID": 5, "AircraftType": "Boeing 737", "Manufacturer": "Boeing", "Layout": "@layout1", "Capacity": 150, "Model": "737-800"},
        {"_id": 6, "AircraftID": 6, "AircraftType": "Airbus A350", "Manufacturer": "Airbus", "Layout": "@layout1", "Capacity": 300, "Model": "A350-900"},
        {"_id": 7, "AircraftID": 7, "AircraftType": "Embraer E175", "Manufacturer": "Embraer", "Layout": "@layout1", "Capacity": 80, "Model": "E175"},
        {"_id": 8, "AircraftID": 8, "AircraftType": "Bombardier CRJ900", "Manufacturer": "Bombardier", "Layout": "@layout1", "Capacity": 90, "Model": "CRJ900"},
        {"_id": 9, "AircraftID": 9, "AircraftType": "Boeing 787", "Manufacturer": "Boeing", "Layout": "@layout1", "Capacity": 250, "Model": "787-9"},
        {"_id": 10, "AircraftID": 10, "AircraftType": "Airbus A330", "Manufacturer": "Airbus", "Layout": "@layout1", "Capacity": 300, "Model": "A330-300"}
    ]
    
    for aircraft in aircraft_data:
        print("Inserting Aircraft:", aircraft)
        inserted_id = insert_aircraft(db, aircraft)

    passenger_data = [
        {"PassportNumber": 12345678, "CustomerName": "John Doe", "Seat_Assigned": "12A", "Disabilities": "None", "Age": 25, "FlightNumber": "FL123", "PhoneNumber": 5551234567},
        {"PassportNumber": 23456789, "CustomerName": "Jane Smith", "Seat_Assigned": "13B", "Disabilities": "Mobility Challenges", "Age": 30, "FlightNumber": "FL124", "PhoneNumber": 5552345678},
        {"PassportNumber": 34567890, "CustomerName": "Alice Johnson", "Seat_Assigned": "14C", "Disabilities": "Visual Impairment", "Age": 28, "FlightNumber": "FL125", "PhoneNumber": 5553456789},
        {"PassportNumber": 45678901, "CustomerName": "Bob Brown", "Seat_Assigned": "15D", "Disabilities": "None", "Age": 45, "FlightNumber": "FL126", "PhoneNumber": 5554567890},
        {"PassportNumber": 56789012, "CustomerName": "Carol White", "Seat_Assigned": "16E", "Disabilities": "Hearing Loss", "Age": 38, "FlightNumber": "FL127", "PhoneNumber": 5555678901},
        {"PassportNumber": 67890123, "CustomerName": "Ahmad Ali", "Seat_Assigned": "21A", "Disabilities": "None", "Age": 34, "FlightNumber": "FL201", "PhoneNumber": 5566789012},
        {"PassportNumber": 78901234, "CustomerName": "Layla Hussein", "Seat_Assigned": "22B", "Disabilities": "None", "Age": 29, "FlightNumber": "FL202", "PhoneNumber": 5567890123},
        {"PassportNumber": 89012345, "CustomerName": "Mohammed Farah", "Seat_Assigned": "23C", "Disabilities": "Visual Impairment", "Age": 42, "FlightNumber": "FL203", "PhoneNumber": 5568901234},
        {"PassportNumber": 90123456, "CustomerName": "Fatima Zahra", "Seat_Assigned": "24D", "Disabilities": "None", "Age": 27, "FlightNumber": "FL204", "PhoneNumber": 5569012345},
        {"PassportNumber": 12378905, "CustomerName": "Yusuf Omar", "Seat_Assigned": "25E", "Disabilities": "Mobility Challenges", "Age": 36, "FlightNumber": "FL205", "PhoneNumber": 5560123456}
    ]

    for passenger in passenger_data:
        print("Inserting Passenger:", passenger["CustomerName"])
        inserted_id = insert_passenger_info(db, passenger)
    flight_data = [
        {"FlightNumber": "FL001", "DepartureAirport": "JFK International Airport", "ArrivalAirport": "Los Angeles International Airport", "FlightDate": "2024-05-01", "DepartureTime": "08:00:00", "ArrivalTime": "11:30:00"},
        {"FlightNumber": "FL002", "DepartureAirport": "Heathrow Airport", "ArrivalAirport": "Charles de Gaulle Airport", "FlightDate": "2024-05-02", "DepartureTime": "10:30:00", "ArrivalTime": "13:45:00"},
        {"FlightNumber": "FL003", "DepartureAirport": "Dubai International Airport", "ArrivalAirport": "Singapore Changi Airport", "FlightDate": "2024-05-03", "DepartureTime": "12:15:00", "ArrivalTime": "18:30:00"},
        {"FlightNumber": "FL004", "DepartureAirport": "Sydney Airport", "ArrivalAirport": "Tokyo Haneda Airport", "FlightDate": "2024-05-04", "DepartureTime": "14:45:00", "ArrivalTime": "20:00:00"},
        {"FlightNumber": "FL005", "DepartureAirport": "Beijing Capital International Airport", "ArrivalAirport": "Hong Kong International Airport", "FlightDate": "2024-05-05", "DepartureTime": "16:30:00", "ArrivalTime": "19:45:00"},
        {"FlightNumber": "FL006", "DepartureAirport": "Cairo International Airport", "ArrivalAirport": "King Abdulaziz International Airport", "FlightDate": "2024-05-06", "DepartureTime": "09:30:00", "ArrivalTime": "12:45:00"},
        {"FlightNumber": "FL007", "DepartureAirport": "Addis Ababa Bole International Airport", "ArrivalAirport": "Hamad International Airport", "FlightDate": "2024-05-07", "DepartureTime": "11:45:00", "ArrivalTime": "16:00:00"},
        {"FlightNumber": "FL008", "DepartureAirport": "Jomo Kenyatta International Airport", "ArrivalAirport": "King Khalid International Airport", "FlightDate": "2024-05-08", "DepartureTime": "13:15:00", "ArrivalTime": "17:30:00"},
        {"FlightNumber": "FL009", "DepartureAirport": "O.R. Tambo International Airport", "ArrivalAirport": "Abu Dhabi International Airport", "FlightDate": "2024-05-09", "DepartureTime": "15:00:00", "ArrivalTime": "19:15:00"},
        {"FlightNumber": "FL010", "DepartureAirport": "Cape Town International Airport", "ArrivalAirport": "Kuwait International Airport", "FlightDate": "2024-05-10", "DepartureTime": "17:30:00", "ArrivalTime": "21:45:00"}
    ]

    for flight in flight_data:
        print("Inserting Flight:", flight["FlightNumber"])
        inserted_id = insert_flight_information(db, flight)
if __name__ == '__main__':
    main()
