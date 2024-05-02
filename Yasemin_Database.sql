CREATE TABLE IF NOT EXISTS Pilot (
	PilotID INT AUTO_INCREMENT PRIMARY KEY,
	PilotName VARCHAR(100),
	LicenseNumber VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS CabinCrew (
	CrewID INT AUTO_INCREMENT PRIMARY KEY,
	Role VARCHAR(100),
	MemberName VARCHAR(100),
	AssignedSeat VARCHAR(10)
);

CREATE TABLE IF NOT EXISTS RosterEntry (
    RosterID INT AUTO_INCREMENT PRIMARY KEY,
    PilotID INT,
    CrewID INT,
    FlightNumber VARCHAR(10),
    Date DATE,
    FOREIGN KEY (PilotID) REFERENCES Pilot(PilotID),
    FOREIGN KEY (CrewID) REFERENCES CabinCrew(CrewID),
    FOREIGN KEY (FlightNumber) REFERENCES FlightInformation(FlightNumber)
);

INSERT INTO Pilot (PilotName, LicenseNumber) VALUES 
    ("Jack Miller", "12345"),
    ("Brian Taylor", "67890"),
    ("Brandon Davis", "54321"),
    ("John Smith", "11111"),
    ("Jane Doe", "22222"),
    ("Michael Johnson", "33333"),
    ("Emily Brown", "44444"),
    ("Chris Wilson", "55555"),
    ("Sarah Thompson", "66666"),
    ("David Martinez", "77777");

INSERT INTO CabinCrew (Role, MemberName, AssignedSeat) VALUES 
    ("First Officer", "Sarah Wilson", "A1"),
    ("Flight Attendant", "Jessica Johnson", "B2"),
    ("Purser", "Kevin White", "C3"),
    ("Cabin Crew", "Alex Martin", "D4"),
    ("Senior Flight Attendant", "Lisa Garcia", "E5"),
    ("Cabin Manager", "Ryan Jones", "F6"),
    ("Junior Flight Attendant", "Michelle Lee", "G7"),
    ("Cabin Attendant", "Andrew Clark", "H8"),
    ("Senior Purser", "Stephanie Rodriguez", "I9"),
    ("Junior Purser", "Tyler Hall", "J10");

INSERT INTO RosterEntry (PilotID, CrewID, FlightNumber, Date) VALUES 
    (1, 1, 'FL001', '2024-05-01'),
    (2, 2, 'FL002', '2024-05-02'),
    (3, 3, 'FL003', '2024-05-03'),
    (4, 4, 'FL004', '2024-05-04'),
    (5, 5, 'FL005', '2024-05-05'),
    (6, 6, 'FL006', '2024-05-06'),
    (7, 7, 'FL007', '2024-05-07'),
    (8, 8, 'FL008', '2024-05-08'),
    (9, 9, 'FL009', '2024-05-09'),
    (10, 10, 'FL010', '2024-05-10');
