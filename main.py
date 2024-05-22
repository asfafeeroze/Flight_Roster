from connect import connectDB
import bson


# INSERT FUNCTIONS TO ADD TO COLLECTIONS
def insert_cabin_crew(db, cabin_crew_data):
    """Inserts a single cabin crew document into the MongoDB collection."""
    cabin_crew_collection = db.cabin_crew
    result = cabin_crew_collection.insert_one(cabin_crew_data)
    return result.inserted_id


def insert_admin(db, admin_data):
    """Inserts a single admin document into the MongoDB collection."""
    if len(admin_data['Password']) < 8:
        raise ValueError("Password must be at least 8 characters long")
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
    if len(passenger_info_data['Password']) < 8:
        raise ValueError("Password must be at least 8 characters long")
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

def get_image_data(image_path):
    try:
        with open(image_path, 'rb') as file:
            return bson.Binary(file.read())
    except FileNotFoundError:
        print(f"Error: File not found - {image_path}")
        return None
        
def update_aircraft_layout(db, aircraft_id, image_path):
    """Updates the layout image of a specific aircraft document."""
    aircraft_collection = db.aircraft
    image_data = get_image_data(image_path)
    if image_data:
        result = aircraft_collection.update_one(
            {'AircraftID': aircraft_id},
            {'$set': {'Layout': image_data}}
        )
        if result.modified_count > 0:
            print(f"Successfully updated layout for aircraft ID {aircraft_id}.")
        else:
            print(f"No aircraft found with ID {aircraft_id} to update.")
    else:
        print(f"Failed to update layout for aircraft ID {aircraft_id} due to image loading issues.")

def user_add_layout(db):
    """Allows the user to add an image to an aircraft entry."""
    aircraft_id = int(input("Enter the Aircraft ID to update: "))
    image_path = input("Enter the full path to the image file: ")
    update_aircraft_layout(db, aircraft_id, image_path)

# Prompt to ask user about data for collections.

def input_document_data(prompts):
    """
    Prompt the user to enter data for fixed keys.
    :param prompts: A dictionary where keys are document keys and values are the prompts for each key.
    :return: A dictionary with the user's data.
    """
    data = {}
    for key, prompt in prompts.items():
        data[key] = input(prompt)  # Input values for each key based on the prompt.
    return data


# QUERIES:

def find_flights_by_airports(db, departure_airport, arrival_airport, flight_date):
    """Retrieve flights from the MongoDB collection based on specified departure and arrival airports on a given date."""
    flight_information_collection = db.flight_information
    flights = list(flight_information_collection.find({
        "DepartureAirport": departure_airport,
        "ArrivalAirport": arrival_airport,
        "FlightDate": flight_date  # Assuming FlightDate is stored as 'YYYY-MM-DD'
    }))
    return flights

def find_flights_by_departure_airport(db, departure_airport, flight_date, arrival_airport=None):
    """Retrieve flights from the MongoDB collection based on specified departure airport, date, and optionally arrival airport."""
    flight_information_collection = db.flight_information
    query = {
        "DepartureAirport": departure_airport,
        "FlightDate": flight_date  # Assuming FlightDate is stored in a consistent format, e.g., 'YYYY-MM-DD'
    }
    if arrival_airport:
        query["ArrivalAirport"] = arrival_airport
    flights = list(flight_information_collection.find(query))
    return flights

def find_flight_by_number(db, flight_number):
    """Retrieve flight information from the MongoDB collection based on the specified flight number."""
    flight_information_collection = db.flight_information
    flight = flight_information_collection.find_one({"FlightNumber": flight_number})
    return flight

def find_passengers_by_flight_number(db, flight_number):
    """Retrieve all passenger information from the MongoDB collection based on the specified flight number."""
    passenger_info_collection = db.passenger_info
    passengers = list(passenger_info_collection.find({"FlightNumber": flight_number}))
    return passengers

def delete_aircraft_by_id(db, aircraft_id):
    """Delete an aircraft record from the MongoDB collection based on the specified aircraft ID."""
    aircraft_collection = db.aircraft
    result = aircraft_collection.delete_one({"AircraftID": aircraft_id})
    return result.deleted_count  # Returns the count of documents deleted

def delete_flight_by_number(db, flight_number):
    """Delete a flight record from the MongoDB collection based on the specified flight number."""
    flight_information_collection = db.flight_information
    result = flight_information_collection.delete_one({"FlightNumber": flight_number})
    return result.deleted_count  # Returns the count of documents deleted

def main():
    db = connectDB()
    
    # Define prompts for each collection
    cabin_crew_prompts = {
        "CrewID": "Enter Crew ID: ",
        "MemberName": "Enter Cabin Crew Member Name: ",
        "Role": "Enter Cabin Crew Role: ",
        "Assigned_Seat": "Enter Assigned Seat (if applicable): "
    }


    aircraft_prompts = {
        "AircraftID": "Enter Aircraft ID: ",
        "Model": "Enter Model: ",
        "Capacity": "Enter Capacity: ",
        "AircraftType": "Enter Aircraft Type: ",
        "Manufacturer": "Enter Manufacturer: ",
        "Layout": "Enter Layout: "
    }

# INPUT AND INSERT FUNCTION FOR AIRCRAFT

    aircraft_data = input_document_data(aircraft_prompts)
    aircraft_id = insert_aircraft(db, aircraft_data)

    passenger_info_prompts = {
        "Email": "Enter Email: ",
        "Password": "Enter Password: ",
        "PassportNumber": "Enter Passport Number: ",
        "CustomerName": "Enter Customer Name: ",
        "Seat_Assigned": "Enter Seat Assigned: ",
        "Disabilities": "Enter any Disabilities: ",
        "Age": "Enter Age: ",
        "PhoneNumber": "Enter Phone Number: "
    }

    flight_info_prompts = {
        "DepartureAirport": "Enter Departure Airport: ",
        "ArrivalAirport": "Enter Arrival Airport: ",
        "DepartureTime": "Enter Departure Time (ISO format): ",
        "ArrivalTime": "Enter Arrival Time (ISO format): ",
        "Date": "Enter Date (YYYY-MM-DD): ",
        "AircraftID": f"Automatically filled Aircraft ID: {aircraft_id}",
        "Price": "Enter Flight Price: ",  # price
    }


    pilot_prompts = {
        "PilotID": "Enter Pilot ID: ",
        "PilotName": "Enter Pilot Name: ",
        "LicenseNumber": "Enter License Number: "
    }

    admin_prompts = {
        "AdminName": "Enter Admin Name: ",
        "Email": "Enter Admin Email: ",
        "Password": "Enter Admin Password"
    }

    # Collect data from user

    flight_information_data = input_document_data(flight_info_prompts)
    flight_information_data['AircraftID'] = aircraft_id  # Ensure aircraft_id is part of flight data
    cabin_crew_data = input_document_data(cabin_crew_prompts)

    pilot_data = input_document_data(pilot_prompts)

    # Insert data into collections

    pilot_id = insert_pilot(db, pilot_data)
    flight_id = insert_flight_information(db, flight_information_data)
    cabin_crew_id = insert_cabin_crew(db, cabin_crew_data)

    # Prepare and insert roster entry data automatically using aircraft_id and flight_id
    roster_entry_data = {
        "FlightNumber": flight_id,
        "PilotID": pilot_id,
        "CrewID": cabin_crew_id,
        "Date": flight_information_data['Date']
    }
    insert_roster_entry(db, roster_entry_data)


# QUERIES
# Function to get all collections in the database
def retrieve_all_from_collection(db, collection_name):
    """Retrieves all documents from the specified collection."""
    collection = db[collection_name]
    documents = list(collection.find())
    return documents

def get_user_by_email(db, email):
    """Retrieve a user document by email."""
    user_collection = db.users
    user_document = user_collection.find_one({"Email": email})
    return user_document

def find_user_by_name(db, name):
    """Find user(s) by name."""
    user_collection = db.users
    users = list(user_collection.find({"Name": name}))
    return users


def update_user_email(db, user_id, new_email):
    """Update user's email based on user_id."""
    user_collection = db.users
    result = user_collection.update_one({"_id": user_id}, {"$set": {"Email": new_email}})
    return result.modified_count

def delete_user_and_related_data_by_id(db, user_id):
    """Delete a user (by ID) and all related data across various collections."""
    # Delete user from 'users' collection
    users_collection = db.users
    user_delete_result = users_collection.delete_one({"_id": user_id})

    # Assuming the user ID is linked in other collections:
    # Delete related passenger info
    passenger_info_collection = db.passenger_info
    passenger_info_delete_result = passenger_info_collection.delete_many({"UserID": user_id})

    # Delete related admin data, if necessary
    admin_collection = db.admins
    admin_delete_result = admin_collection.delete_many({"UserID": user_id})

    # Other deletions can be added here similarly

    # Return a summary of deletion results
    return {
        "User Deleted": user_delete_result.deleted_count,
        "Passenger Info Deleted": passenger_info_delete_result.deleted_count,
        "Admin Data Deleted": admin_delete_result.deleted_count,
        # Include additional collections if necessary
    }

def delete_user_and_related_data_by_name(db, name):
    """Delete users and all related data across various collections by name."""
    users_collection = db.users
    # Find all users with the given name to delete them and their related data
    user_documents = users_collection.find({"Name": name})

    deleted_users_count = 0
    passenger_info_deleted_count = 0
    admin_data_deleted_count = 0

    for user_doc in user_documents:
        user_id = user_doc['_id']

        # Delete user
        user_delete_result = users_collection.delete_one({"_id": user_id})
        deleted_users_count += user_delete_result.deleted_count

        # Assuming the user ID is linked in other collections:
        # Delete related passenger info
        passenger_info_collection = db.passenger_info
        passenger_info_delete_result = passenger_info_collection.delete_many({"UserID": user_id})
        passenger_info_deleted_count += passenger_info_delete_result.deleted_count

        # Delete related admin data, if necessary
        admin_collection = db.admins
        admin_delete_result = admin_collection.delete_many({"UserID": user_id})
        admin_data_deleted_count += admin_delete_result.deleted_count

    # Return a summary of deletion results
    if deleted_users_count == 0:
        return "No user found with the provided name."

    return {
        "Users Deleted": deleted_users_count,
        "Passenger Info Deleted": passenger_info_deleted_count,
        "Admin Data Deleted": admin_data_deleted_count,
    }


def delete_flight_roster_and_related_data(db, flight_number):
    """Delete a flight roster entry and all related data."""
    # Delete the roster entry
    roster_collection = db.roster_entry
    roster_delete_result = roster_collection.delete_one({"FlightNumber": flight_number})

    if roster_delete_result.deleted_count == 0:
        return "No roster found with the provided flight number."

    # Assuming related data needs to be deleted or updated
    # Delete related flight information
    flight_info_collection = db.flight_information
    flight_info_delete_result = flight_info_collection.delete_many({"FlightNumber": flight_number})

    # Delete or update crew assignments
    crew_collection = db.crew_assignments
    crew_delete_result = crew_collection.delete_many({"FlightNumber": flight_number})

    # Delete or update passenger bookings
    passenger_booking_collection = db.passenger_bookings
    passenger_booking_delete_result = passenger_booking_collection.delete_many({"FlightNumber": flight_number})

    # Return a summary of deletion results
    return {
        "Roster Deleted": roster_delete_result.deleted_count,
        "Flight Info Deleted": flight_info_delete_result.deleted_count,
        "Crew Assignments Deleted": crew_delete_result.deleted_count,
        "Passenger Bookings Deleted": passenger_booking_delete_result.deleted_count,
    }

    # Parts for adding the information to MongoDB.

    #    layout_images = {
    #        1: r'C:\Users\Randa Amin\OneDrive\Desktop\CS308\layout1.png',
    #        2: r'C:\Users\Randa Amin\OneDrive\Desktop\CS308\layout1.png',
    #        3: r'C:\Users\Randa Amin\OneDrive\Desktop\CS308\layout1.png',
    #        # Add paths for all aircraft
    #    }
    #    aircraft_data = [
    #        {"_id": 1, "AircraftID": 1, "AircraftType": "Boeing 747", "Manufacturer": "Boeing", "Layout": get_image_data(layout_images[1]), "Capacity": 500, "Model": "747-400"},
    #        {"_id": 2, "AircraftID": 2, "AircraftType": "Airbus A320", "Manufacturer": "Airbus", "Layout": get_image_data(layout_images[1]), "Capacity": 200, "Model": "A320neo"},
    #        {"_id": 3, "AircraftID": 3, "AircraftType": "Boeing 777", "Manufacturer": "Boeing", "Layout": get_image_data(layout_images[1]), "Capacity": 400, "Model": "777-300ER"},
    #        {"_id": 4, "AircraftID": 4, "AircraftType": "Airbus A380", "Manufacturer": "Airbus", "Layout": get_image_data(layout_images[1]), "Capacity": 800, "Model": "A380-800"},
    #        {"_id": 5, "AircraftID": 5, "AircraftType": "Boeing 737", "Manufacturer": "Boeing", "Layout": get_image_data(layout_images[1]), "Capacity": 150, "Model": "737-800"},
    #        {"_id": 6, "AircraftID": 6, "AircraftType": "Airbus A350", "Manufacturer": "Airbus", "Layout": get_image_data(layout_images[1]), "Capacity": 300, "Model": "A350-900"},
    #        {"_id": 7, "AircraftID": 7, "AircraftType": "Embraer E175", "Manufacturer": "Embraer", "Layout": get_image_data(layout_images[1]), "Capacity": 80, "Model": "E175"},
    #        {"_id": 8, "AircraftID": 8, "AircraftType": "Bombardier CRJ900", "Manufacturer": "Bombardier", "Layout": get_image_data(layout_images[1]), "Capacity": 90, "Model": "CRJ900"},
    #        {"_id": 9, "AircraftID": 9, "AircraftType": "Boeing 787", "Manufacturer": "Boeing", "Layout": get_image_data(layout_images[1]), "Capacity": 250, "Model": "787-9"},
    #        {"_id": 10, "AircraftID": 10, "AircraftType": "Airbus A330", "Manufacturer": "Airbus", "Layout": get_image_data(layout_images[1]), "Capacity": 300, "Model": "A330-300"}
    #    ]

    #  for aircraft in aircraft_data:
    #        print("Inserting Aircraft:", aircraft["AircraftID"])
    #        if aircraft["Layout"] is not None:  # Only insert if the layout image was found and loaded
    #            inserted_id = insert_aircraft(db, aircraft)
    #            print(f"Aircraft ID {aircraft['AircraftID']} inserted with ID: {inserted_id}")
    #        else:
    #            print(f"Failed to insert Aircraft ID {aircraft['AircraftID']}: Layout image not found")

    # # Sample passenger data with the specified attributes
    # passenger_data = [
    #     {
    #         "Email": "john.doe@example.com", "Password": "password123", "PassportNumber": 12345678,
    #         "CustomerName": "John Doe", "Seat_Assigned": "12A", "Disabilities": "None", "Age": 25,
    #         "FlightNumber": "FL123", "PhoneNumber": 5551234567
    #     },
    #     {
    #         "Email": "jane.smith@example.com", "Password": "password234", "PassportNumber": 23456789,
    #         "CustomerName": "Jane Smith", "Seat_Assigned": "13B", "Disabilities": "Mobility Challenges", "Age": 30,
    #         "FlightNumber": "FL124", "PhoneNumber": 5552345678
    #     },
    #     {
    #         "Email": "alice.johnson@example.com", "Password": "password345", "PassportNumber": 34567890,
    #         "CustomerName": "Alice Johnson", "Seat_Assigned": "14C", "Disabilities": "Visual Impairment", "Age": 28,
    #         "FlightNumber": "FL125", "PhoneNumber": 5553456789
    #     },
    #     {
    #         "Email": "bob.brown@example.com", "Password": "password456", "PassportNumber": 45678901,
    #         "CustomerName": "Bob Brown", "Seat_Assigned": "15D", "Disabilities": "None", "Age": 45,
    #         "FlightNumber": "FL126", "PhoneNumber": 5554567890
    #     },
    #     {
    #         "Email": "carol.white@example.com", "Password": "password567", "PassportNumber": 56789012,
    #         "CustomerName": "Carol White", "Seat_Assigned": "16E", "Disabilities": "Hearing Loss", "Age": 38,
    #         "FlightNumber": "FL127", "PhoneNumber": 5555678901
    #     },
    #     {
    #         "Email": "ahmad.ali@example.com", "Password": "password678", "PassportNumber": 67890123,
    #         "CustomerName": "Ahmad Ali", "Seat_Assigned": "21A", "Disabilities": "None", "Age": 34,
    #         "FlightNumber": "FL201", "PhoneNumber": 5566789012
    #     },
    #     {
    #         "Email": "layla.hussein@example.com", "Password": "password789", "PassportNumber": 78901234,
    #         "CustomerName": "Layla Hussein", "Seat_Assigned": "22B", "Disabilities": "None", "Age": 29,
    #         "FlightNumber": "FL202", "PhoneNumber": 5567890123
    #     },
    #     {
    #         "Email": "mohammed.farah@example.com", "Password": "password890", "PassportNumber": 89012345,
    #         "CustomerName": "Mohammed Farah", "Seat_Assigned": "23C", "Disabilities": "Visual Impairment", "Age": 42,
    #         "FlightNumber": "FL203", "PhoneNumber": 5568901234
    #     },
    #     {
    #         "Email": "fatima.zahra@example.com", "Password": "password901", "PassportNumber": 90123456,
    #         "CustomerName": "Fatima Zahra", "Seat_Assigned": "24D", "Disabilities": "None", "Age": 27,
    #         "FlightNumber": "FL204", "PhoneNumber": 5569012345
    #     },
    #     {
    #         "Email": "yusuf.omar@example.com", "Password": "password012", "PassportNumber": 12378905,
    #         "CustomerName": "Yusuf Omar", "Seat_Assigned": "25E", "Disabilities": "Mobility Challenges", "Age": 36,
    #         "FlightNumber": "FL205", "PhoneNumber": 5560123456
    #     }
    # ]

    #     for passenger in passenger_data:
    # try:
    #         insert_passenger_info(db, passenger_info_data)
    #     except ValueError as e:
    #         print(e)
    #         return

    #    flight_data = [
    #        {"FlightNumber": "FL001", "DepartureAirport": "JFK International Airport", "ArrivalAirport": "Los Angeles International Airport", "FlightDate": "2024-05-01", "DepartureTime": "08:00:00", "ArrivalTime": "11:30:00"},
    #        {"FlightNumber": "FL002", "DepartureAirport": "Heathrow Airport", "ArrivalAirport": "Charles de Gaulle Airport", "FlightDate": "2024-05-02", "DepartureTime": "10:30:00", "ArrivalTime": "13:45:00"},
    #        {"FlightNumber": "FL003", "DepartureAirport": "Dubai International Airport", "ArrivalAirport": "Singapore Changi Airport", "FlightDate": "2024-05-03", "DepartureTime": "12:15:00", "ArrivalTime": "18:30:00"},
    #        {"FlightNumber": "FL004", "DepartureAirport": "Sydney Airport", "ArrivalAirport": "Tokyo Haneda Airport", "FlightDate": "2024-05-04", "DepartureTime": "14:45:00", "ArrivalTime": "20:00:00"},
    #        {"FlightNumber": "FL005", "DepartureAirport": "Beijing Capital International Airport", "ArrivalAirport": "Hong Kong International Airport", "FlightDate": "2024-05-05", "DepartureTime": "16:30:00", "ArrivalTime": "19:45:00"},
    #        {"FlightNumber": "FL006", "DepartureAirport": "Cairo International Airport", "ArrivalAirport": "King Abdulaziz International Airport", "FlightDate": "2024-05-06", "DepartureTime": "09:30:00", "ArrivalTime": "12:45:00"},
    #        {"FlightNumber": "FL007", "DepartureAirport": "Addis Ababa Bole International Airport", "ArrivalAirport": "Hamad International Airport", "FlightDate": "2024-05-07", "DepartureTime": "11:45:00", "ArrivalTime": "16:00:00"},
    #        {"FlightNumber": "FL008", "DepartureAirport": "Jomo Kenyatta International Airport", "ArrivalAirport": "King Khalid International Airport", "FlightDate": "2024-05-08", "DepartureTime": "13:15:00", "ArrivalTime": "17:30:00"},
    #        {"FlightNumber": "FL009", "DepartureAirport": "O.R. Tambo International Airport", "ArrivalAirport": "Abu Dhabi International Airport", "FlightDate": "2024-05-09", "DepartureTime": "15:00:00", "ArrivalTime": "19:15:00"},
    #        {"FlightNumber": "FL010", "DepartureAirport": "Cape Town International Airport", "ArrivalAirport": "Kuwait International Airport", "FlightDate": "2024-05-10", "DepartureTime": "17:30:00", "ArrivalTime": "21:45:00"}
    #    ]

    #    for flight in flight_data:
    #        print("Inserting Flight:", flight["FlightNumber"])
    #        inserted_id = insert_flight_information(db, flight)
    # flights_collection = db["flight_information"]


# # adding the flight price data.
#     flight_data = [
#         {"FlightNumber": "FL001", "Price": 300},
#         {"FlightNumber": "FL002", "Price": 150},
#         {"FlightNumber": "FL003", "Price": 500},
#         {"FlightNumber": "FL004", "Price": 450},
#         {"FlightNumber": "FL005", "Price": 200},
#         {"FlightNumber": "FL006", "Price": 250},
#         {"FlightNumber": "FL007", "Price": 350},
#         {"FlightNumber": "FL008", "Price": 400},
#         {"FlightNumber": "FL009", "Price": 600},
#         {"FlightNumber": "FL010", "Price": 550}
#     ]

# # Update each flight document with the new price
#     for flight in flight_data:
#         flight_number = flight["FlightNumber"]
#         price = flight["Price"]

#         result = flights_collection.update_one(
#             {"FlightNumber": flight_number},  # Find the document by FlightNumber
#             {"$set": {"Price": price}}        # Set the new Price field
#     )

#    pilot_data = [
#        {"PilotID": 1, "PilotName": "Jack Miller", "LicenseNumber": "12345"},
#        {"PilotID": 2, "PilotName": "Brian Taylor", "LicenseNumber": "67890"},
#        {"PilotID": 3, "PilotName": "Brandon Davis", "LicenseNumber": "54321"},
#        {"PilotID": 4, "PilotName": "John Smith", "LicenseNumber": "11111"},
#        {"PilotID": 5, "PilotName": "Jane Doe", "LicenseNumber": "22222"},
#        {"PilotID": 6, "PilotName": "Michael Johnson", "LicenseNumber": "33333"},
#        {"PilotID": 7, "PilotName": "Emily Brown", "LicenseNumber": "44444"},
#        {"PilotID": 8, "PilotName": "Chris Wilson", "LicenseNumber": "55555"},
#        {"PilotID": 9, "PilotName": "Sarah Thompson", "LicenseNumber": "66666"},
#        {"PilotID": 10, "PilotName": "David Martinez", "LicenseNumber": "77777"}
#    ]

#    for pilots_data in pilot_data:
#        insert_pilot(db, pilots_data)

#    cabin_crew_data = [
#        {"CrewID": 1, "Role": "First Officer", "MemberName": "Sarah Wilson", "AssignedSeat": "A1"},
#        {"CrewID": 2, "Role": "Flight Attendant", "MemberName": "Jessica Johnson", "AssignedSeat": "B2"},
#        {"CrewID": 3, "Role": "Purser", "MemberName": "Kevin White", "AssignedSeat": "C3"},
#        {"CrewID": 4, "Role": "Cabin Crew", "MemberName": "Alex Martin", "AssignedSeat": "D4"},
#        {"CrewID": 5, "Role": "Senior Flight Attendant", "MemberName": "Lisa Garcia", "AssignedSeat": "E5"},
#        {"CrewID": 6, "Role": "Cabin Manager", "MemberName": "Ryan Jones", "AssignedSeat": "F6"},
#        {"CrewID": 7, "Role": "Junior Flight Attendant", "MemberName": "Michelle Lee", "AssignedSeat": "G7"},
#        {"CrewID": 8, "Role": "Cabin Attendant", "MemberName": "Andrew Clark", "AssignedSeat": "H8"},
#        {"CrewID": 9, "Role": "Senior Purser", "MemberName": "Stephanie Rodriguez", "AssignedSeat": "I9"},
#        {"CrewID": 10, "Role": "Junior Purser", "MemberName": "Tyler Hall", "AssignedSeat": "J10"}
#    ]

#    for crew_data in cabin_crew_data:
#        insert_cabin_crew(db, crew_data)

#    roster_entry_data = [
#        {"RosterID": 1, "PilotID": 1, "CrewID": 1, "FlightNumber": "FL001", "Date": "2024-05-01"},
#        {"RosterID": 2, "PilotID": 2, "CrewID": 2, "FlightNumber": "FL001", "Date": "2024-05-02"},
#        {"RosterID": 3, "PilotID": 3, "CrewID": 3, "FlightNumber": "FL001", "Date": "2024-05-03"},
#        {"RosterID": 4, "PilotID": 4, "CrewID": 4, "FlightNumber": "FL001", "Date": "2024-05-04"},
#        {"RosterID": 5, "PilotID": 5, "CrewID": 5, "FlightNumber": "FL001", "Date": "2024-05-05"},
#        {"RosterID": 6, "PilotID": 6, "CrewID": 6, "FlightNumber": "FL001", "Date": "2024-05-06"},
#        {"RosterID": 7, "PilotID": 7, "CrewID": 7, "FlightNumber": "FL001", "Date": "2024-05-07"},
#        {"RosterID": 8, "PilotID": 8, "CrewID": 8, "FlightNumber": "FL001", "Date": "2024-05-08"},
#        {"RosterID": 9, "PilotID": 9, "CrewID": 9, "FlightNumber": "FL001", "Date": "2024-05-09"},
#        {"RosterID": 10, "PilotID": 10, "CrewID": 10, "FlightNumber": "FL001", "Date": "2024-05-10"}
#    ]

#    for entry_data in roster_entry_data:
#        insert_roster_entry(db, entry_data)

#    admin_data = [
#        {"AdminName": "Admin1", "Email": "user1@example.com", "Password": "password1"},
#        {"AdminName": "Admin2", "Email": "user2@example.com", "Password": "password2"},
#        {"AdminName": "Admin3", "Email": "user3@example.com", "Password": "password3"},
#        {"AdminName": "Admin4", "Email": "user4@example.com", "Password": "password4"},
#        {"AdminName": "Admin5", "Email": "user5@example.com", "Password": "password5"},
#        {"AdminName": "Admin6", "Email": "user6@example.com", "Password": "password6"},
#        {"AdminName": "Admin7", "Email": "user7@example.com", "Password": "password7"},
#        {"AdminName": "Admin8", "Email": "user8@example.com", "Password": "password8"},
#        {"AdminName": "Admin9", "Email": "user9@example.com", "Password": "password9"},
#        {"AdminName": "Admin10", "Email": "user10@example.com", "Password": "password10"}
#    ]

#    for data in admin_data:
#        insert_admin(db, data)

# Example usage for connect.py functions:
# data = {
#     "column1": "value1",
#     "column2": "value2"
# }
#
# # Connect to MySQL
# engine, session = connect_mysql()
# store_roster_mysql(engine, session, data)
# retrieved_rosters_mysql = retrieve_roster_mysql(session)
# print("Retrieved rosters from MySQL:", retrieved_rosters_mysql)
#
# # Connect to MongoDB
# db = connect_nosql()
# store_roster_nosql(db, data)
# retrieved_rosters_nosql = retrieve_roster_nosql(db)
# print("Retrieved rosters from MongoDB:", retrieved_rosters_nosql)
#
# # Export to JSON file
# export_roster_to_json(retrieved_rosters_mysql, 'roster_mysql.json')
# export_roster_to_json(retrieved_rosters_nosql, 'roster_nosql.json')


if __name__ == '__main__':
    main()
