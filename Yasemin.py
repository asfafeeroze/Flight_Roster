
from connect import connectDB


def insert_aircraft(db, aircraft_data):
    aircraft_collection = db.aircraft
    result = aircraft_collection.insert_one(aircraft_data)
    print(f"Inserted aircraft with ID: {result.inserted_id}")


def insert_flight_information(db, flight_information_data):
    flight_information_collection = db.flight_information
    result = flight_information_collection.insert_one(flight_information_data)
    print(f"Inserted flight information with ID: {result.inserted_id}")


def insert_pilot(db, pilot_data):
    pilot_collection = db.Pilot
    result = pilot_collection.insert_one(pilot_data)
    print(f"Inserted pilot with ID: {result.inserted_id}")


def insert_cabin_crew(db, cabin_crew_data):
    cabin_crew_collection = db.CabinCrew
    result = cabin_crew_collection.insert_one(cabin_crew_data)
    print(f"Inserted cabin crew member with ID: {result.inserted_id}")


def insert_roster_entry(db, roster_entry_data):
    roster_entry_collection = db.RosterEntry
    result = roster_entry_collection.insert_one(roster_entry_data)
    print(f"Inserted roster entry with ID: {result.inserted_id}")


def insert_admin(db, admin_data):
    admin_collection = db.Admin
    result = admin_collection.insert_one(admin_data)
    print(f"Inserted admin with ID: {result.inserted_id}")


if __name__ == '__main__':
    db = connectDB()

    flight_information_data = {
        "FlightNumber": "FL001",
        "DepartureAirport": "JFK",
        "ArrivalAirport": "LAX",
        "DepartureTime": "2024-05-01T15:00:00Z",
        "ArrivalTime": "2024-05-01T18:00:00Z",
        "Date": "2024-05-01",
        "AircraftID": "aircraft_identifier"
    }

    aircraft_data = {
        "AircraftID": "A123",
        "Model": "Boeing 737",
        "Capacity": 188,
        "AircraftType": "Commercial",
        "Manufacturer": "Boeing",
        "Layout": "Standard"
    }

    pilot_data = [
        {"PilotID": 1, "PilotName": "Jack Miller", "LicenseNumber": "12345"},
        {"PilotID": 2, "PilotName": "Brian Taylor", "LicenseNumber": "67890"},
        {"PilotID": 3, "PilotName": "Brandon Davis", "LicenseNumber": "54321"},
        {"PilotID": 4, "PilotName": "John Smith", "LicenseNumber": "11111"},
        {"PilotID": 5, "PilotName": "Jane Doe", "LicenseNumber": "22222"},
        {"PilotID": 6, "PilotName": "Michael Johnson", "LicenseNumber": "33333"},
        {"PilotID": 7, "PilotName": "Emily Brown", "LicenseNumber": "44444"},
        {"PilotID": 8, "PilotName": "Chris Wilson", "LicenseNumber": "55555"},
        {"PilotID": 9, "PilotName": "Sarah Thompson", "LicenseNumber": "66666"},
        {"PilotID": 10, "PilotName": "David Martinez", "LicenseNumber": "77777"}
    ]

    cabin_crew_data = [
        {"CrewID": 1, "Role": "First Officer", "MemberName": "Sarah Wilson", "AssignedSeat": "A1"},
        {"CrewID": 2, "Role": "Flight Attendant", "MemberName": "Jessica Johnson", "AssignedSeat": "B2"},
        {"CrewID": 3, "Role": "Purser", "MemberName": "Kevin White", "AssignedSeat": "C3"},
        {"CrewID": 4, "Role": "Cabin Crew", "MemberName": "Alex Martin", "AssignedSeat": "D4"},
        {"CrewID": 5, "Role": "Senior Flight Attendant", "MemberName": "Lisa Garcia", "AssignedSeat": "E5"},
        {"CrewID": 6, "Role": "Cabin Manager", "MemberName": "Ryan Jones", "AssignedSeat": "F6"},
        {"CrewID": 7, "Role": "Junior Flight Attendant", "MemberName": "Michelle Lee", "AssignedSeat": "G7"},
        {"CrewID": 8, "Role": "Cabin Attendant", "MemberName": "Andrew Clark", "AssignedSeat": "H8"},
        {"CrewID": 9, "Role": "Senior Purser", "MemberName": "Stephanie Rodriguez", "AssignedSeat": "I9"},
        {"CrewID": 10, "Role": "Junior Purser", "MemberName": "Tyler Hall", "AssignedSeat": "J10"}
    ]

    roster_entry_data = [
        {"RosterID": 1, "PilotID": 1, "CrewID": 1, "FlightNumber": "FL001", "Date": "2024-05-01"},
        {"RosterID": 2, "PilotID": 2, "CrewID": 2, "FlightNumber": "FL001", "Date": "2024-05-02"},
        {"RosterID": 3, "PilotID": 3, "CrewID": 3, "FlightNumber": "FL001", "Date": "2024-05-03"},
        {"RosterID": 4, "PilotID": 4, "CrewID": 4, "FlightNumber": "FL001", "Date": "2024-05-04"},
        {"RosterID": 5, "PilotID": 5, "CrewID": 5, "FlightNumber": "FL001", "Date": "2024-05-05"},
        {"RosterID": 6, "PilotID": 6, "CrewID": 6, "FlightNumber": "FL001", "Date": "2024-05-06"},
        {"RosterID": 7, "PilotID": 7, "CrewID": 7, "FlightNumber": "FL001", "Date": "2024-05-07"},
        {"RosterID": 8, "PilotID": 8, "CrewID": 8, "FlightNumber": "FL001", "Date": "2024-05-08"},
        {"RosterID": 9, "PilotID": 9, "CrewID": 9, "FlightNumber": "FL001", "Date": "2024-05-09"},
        {"RosterID": 10, "PilotID": 10, "CrewID": 10, "FlightNumber": "FL001", "Date": "2024-05-10"}
    ]

    admin_data = [
        {"AdminName": "Admin1", "Email": "user1@example.com", "Password": "password1"},
        {"AdminName": "Admin2", "Email": "user2@example.com", "Password": "password2"},
        {"AdminName": "Admin3", "Email": "user3@example.com", "Password": "password3"},
        {"AdminName": "Admin4", "Email": "user4@example.com", "Password": "password4"},
        {"AdminName": "Admin5", "Email": "user5@example.com", "Password": "password5"},
        {"AdminName": "Admin6", "Email": "user6@example.com", "Password": "password6"},
        {"AdminName": "Admin7", "Email": "user7@example.com", "Password": "password7"},
        {"AdminName": "Admin8", "Email": "user8@example.com", "Password": "password8"},
        {"AdminName": "Admin9", "Email": "user9@example.com", "Password": "password9"},
        {"AdminName": "Admin10", "Email": "user10@example.com", "Password": "password10"}
    ]

    insert_aircraft(db, aircraft_data)

    insert_flight_information(db, flight_information_data)

    for data in pilot_data:
        insert_pilot(db, data)

    for data in cabin_crew_data:
        insert_cabin_crew(db, data)

    for data in roster_entry_data:
        insert_roster_entry(db, data)

    for data in admin_data:
        insert_admin(db, data)

