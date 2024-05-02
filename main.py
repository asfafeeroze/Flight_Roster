from connect import connectDB

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


def main():
    db = connectDB()

    # Define prompts for each collection
    user_prompts = {
        "Email": "Enter User Email: ",
        "Password": "Enter User Password: ",
        "Role": "Enter Role (Passenger/Admin): "
    }

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

# INPUT AND INSERT FUNCTION FOR USER AND AIRCRAFT
    user_data = input_document_data(user_prompts)
    user_id = insert_user(db, user_data)  # Store user data with role

    aircraft_data = input_document_data(aircraft_prompts)
    aircraft_id = insert_aircraft(db, aircraft_data)

    passenger_info_prompts = {
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
    }

    pilot_prompts = {
        "PilotID": "Enter Pilot ID: ",
        "PilotName": "Enter Pilot Name: ",
        "LicenseNumber": "Enter License Number: "
    }

    admin_prompts = {
        "AdminName": "Enter Admin Name: ",
        "PhoneNumber": "Enter Admin Phone Number: "
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

    if user_data['Role'].lower() == 'passenger':
        passenger_info_prompts = {
            "PassportNumber": "Enter Passport Number: ",
            "CustomerName": "Enter Customer Name: ",
            "Seat_Assigned": "Enter Seat Assigned: ",
            "Disabilities": "Enter any Disabilities: ",
            "Age": "Enter Age: ",
            "PhoneNumber": "Enter Phone Number: ",
            "UserID": user_id  # Linking passenger info to user
        }
        passenger_info_data = input_document_data(passenger_info_prompts)
        insert_passenger_info(db, passenger_info_data)
    elif user_data['Role'].lower() == 'admin':
        admin_prompts = {
            "AdminName": "Enter Admin Name: ",
            "PhoneNumber": "Enter Admin Phone Number: ",
            "UserID": user_id  # Linking admin info to user
        }
        admin_data = input_document_data(admin_prompts)
        insert_admin(db, admin_data)

    # Prepare and insert roster entry data automatically using aircraft_id and flight_id
    roster_entry_data = {
        "FlightNumber": flight_id,
        "PilotID": pilot_id,
        "CrewID": cabin_crew_id,
        "Date": flight_information_data['Date']
    }
    insert_roster_entry(db, roster_entry_data)




if __name__ == '__main__':
    main()
