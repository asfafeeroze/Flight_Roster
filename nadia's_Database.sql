CREATE DATABASE cs308_database;
USE cs308_database;
Create table Passenger (
    Id INT int NOT NULL AUTO_INCREMENT,
    PassportNumber INT unique,
    CustomerName char(100)CHARACTER SET utf8mb4,
    Seat_Assigned varchar(5),
    Disabilities Text,
    Age int,
    FlightNumber varchar(10),
    PhoneNumber varchar(20),
    PRIMARY KEY (Id)
    
);


INSERT INTO Passenger (Email, Password, PassportNumber, CustomerName, Seat_Assigned, Disabilities, Age, FlightNumber, PhoneNumber) VALUES
(12345678, 'John Doe', '12A', 'None', 25, 'FL123', 5551234567),
(23456789, 'Jane Smith', '13B', 'Mobility Challenges', 30, 'FL124', 5552345678),
(34567890, 'Alice Johnson', '14C', 'Visual Impairment', 28, 'FL125', 5553456789),
(45678901, 'Bob Brown', '15D', 'None', 45, 'FL126', 5554567890),
(56789012, 'Carol White', '16E', 'Hearing Loss', 38, 'FL127', 5555678901),
(67890123, 'Ahmad Ali', '21A', 'None', 34, 'FL201', 5566789012),
(78901234, 'Layla Hussein', '22B', 'None', 29, 'FL202', 5567890123),
(89012345, 'Mohammed Farah', '23C', 'Visual Impairment', 42, 'FL203', 5568901234),
(90123456, 'Fatima Zahra', '24D', 'None', 27, 'FL204', 5569012345),
(01234567, 'Yusuf Omar', '25E', 'Mobility Challenges', 36, 'FL205', 5560123456);
DROP TABLE users;
ALTER TABLE passenger
DROP COLUMN PassengerID;
ALTER TABLE passenger
ADD COLUMN Email VARCHAR(50),
ADD COLUMN Passwords VARCHAR(50);
ALTER TABLE passenger
ADD PRIMARY KEY (Email);

-- Update for John Doe
UPDATE passenger
SET Email = 'john.doe@example.com', Passwords = 'password123'
WHERE PassportNumber = 12345678;

-- Update for Jane Smith
UPDATE passenger
SET Email = 'jane.smith@example.com', Passwords = 'password234'
WHERE PassportNumber = 23456789;

-- Update for Alice Johnson
UPDATE passenger
SET Email = 'alice.johnson@example.com', Passwords = 'password345'
WHERE PassportNumber = 34567890;

-- Update for Bob Brown
UPDATE passenger
SET Email = 'bob.brown@example.com', Passwords = 'password456'
WHERE PassportNumber = 45678901;

-- Update for Carol White
UPDATE passenger
SET Email = 'carol.white@example.com', Passwords = 'password567'
WHERE PassportNumber = 56789012;

-- Update for Ahmad Ali
UPDATE passenger
SET Email = 'ahmad.ali@example.com', Passwords = 'password678'
WHERE PassportNumber = 67890123;

-- Update for Layla Hussein
UPDATE passenger
SET Email = 'layla.hussein@example.com', Passwords = 'password789'
WHERE PassportNumber = 78901234;

-- Update for Mohammed Farah
UPDATE passenger
SET Email = 'mohammed.farah@example.com', Passwords = 'password890'
WHERE PassportNumber = 89012345;

-- Update for Fatima Zahra
UPDATE passenger
SET Email = 'fatima.zahra@example.com', Passwords = 'password901'
WHERE PassportNumber = 90123456;

-- Update for Yusuf Omar
UPDATE passenger
SET Email = 'yusuf.omar@example.com', Passwords = 'password012'
WHERE PassportNumber = 1234567;


DELIMITER //

CREATE TRIGGER before_insert_passenger
BEFORE INSERT ON passenger
FOR EACH ROW
BEGIN
    IF LENGTH(NEW.Passwords) < 8 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Password must be at least 8 characters long';
    END IF;
END;

//

DELIMITER ;
DELIMITER //

CREATE TRIGGER before_update_passenger
BEFORE UPDATE ON passenger
FOR EACH ROW
BEGIN
    IF LENGTH(NEW.Passwords) < 8 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Password must be at least 8 characters long';
    END IF;
END;

//

DELIMITER ;


Create table Aircraft (
	AircraftID int,
    AircraftType varchar(100),
    Manufacturer varchar(100),
    Layout Blob,
    Capacity int,
    Model varchar(50),
    PRIMARY KEY (AircraftID)
);

INSERT INTO Aircraft (AircraftID, AircraftType, Manufacturer, Layout, Capacity, Model)
VALUES
    (1, 'Boeing 747', 'Boeing', @layout1, 500, '747-400'),
    (2, 'Airbus A320', 'Airbus', @layout1, 200, 'A320neo'),
    (3, 'Boeing 777', 'Boeing', @layout1, 400, '777-300ER'),
    (4, 'Airbus A380', 'Airbus', @layout1, 800, 'A380-800'),
    (5, 'Boeing 737', 'Boeing', @layout1, 150, '737-800'),
    (6, 'Airbus A350', 'Airbus', @layout1, 300, 'A350-900'),
    (7, 'Embraer E175', 'Embraer', @layout1, 80, 'E175'),
    (8, 'Bombardier CRJ900', 'Bombardier', @layout1, 90, 'CRJ900'),
    (9, 'Boeing 787', 'Boeing', @layout1, 250, '787-9'),
    (10, 'Airbus A330', 'Airbus', @layout1, 300, 'A330-300');
    
UPDATE Aircraft
SET Layout = LOAD_FILE('\Users\Randa Amin\OneDrive\Desktop\CS308\layout1.png')  
WHERE AircraftID = 1;
Create table FlightInformation (
	FlightNumber varchar(10),
    DepartureAirport varchar(100),
    ArrivalAirport varchar(100),
    FlightDate date,
    DepartureTime TIME,
    ArrivalTime Time,
    PRIMARY KEY (FlightNumber)
    
);
INSERT INTO FlightInformation (FlightNumber, DepartureAirport, ArrivalAirport, FlightDate, DepartureTime, ArrivalTime)
VALUES
    ('FL001', 'JFK International Airport', 'Los Angeles International Airport', '2024-05-01', '08:00:00', '11:30:00'),
    ('FL002', 'Heathrow Airport', 'Charles de Gaulle Airport', '2024-05-02', '10:30:00', '13:45:00'),
    ('FL003', 'Dubai International Airport', 'Singapore Changi Airport', '2024-05-03', '12:15:00', '18:30:00'),
    ('FL004', 'Sydney Airport', 'Tokyo Haneda Airport', '2024-05-04', '14:45:00', '20:00:00'),
    ('FL005', 'Beijing Capital International Airport', 'Hong Kong International Airport', '2024-05-05', '16:30:00', '19:45:00'),
	('FL006', 'Cairo International Airport', 'King Abdulaziz International Airport', '2024-05-06', '09:30:00', '12:45:00'),
    ('FL007', 'Addis Ababa Bole International Airport', 'Hamad International Airport', '2024-05-07', '11:45:00', '16:00:00'),
    ('FL008', 'Jomo Kenyatta International Airport', 'King Khalid International Airport', '2024-05-08', '13:15:00', '17:30:00'),
    ('FL009', 'O.R. Tambo International Airport', 'Abu Dhabi International Airport', '2024-05-09', '15:00:00', '19:15:00'),
    ('FL010', 'Cape Town International Airport', 'Kuwait International Airport', '2024-05-10', '17:30:00', '21:45:00');

