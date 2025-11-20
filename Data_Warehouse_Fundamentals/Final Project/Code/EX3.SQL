-- Load data into the Data Warehouse
-- Create tables DimDate, DimStation, DimTruck, and FactTrips

-- Create tables DimDate  --
CREATE TABLE DimDate (
	Dateid INT NOT NULL PRIMARY KEY,
	Date DATE NOT NULL,
	Year INT NOT NULL,
	Quarter INT NOT NULL,
	QuarterName VARCHAR(50) NOT NULL,
	Month INT NOT NULL,
	Monthname VARCHAR(50) NOT NULL,
    Day INT NOT NULL,
	Weekday INT NOT NULL,
	WeekdayName VARCHAR(50) NOT NULL
);
-- Create tables DimTruck  --
CREATE TABLE DimTruck(
	Truckid INT NOT NULL PRIMARY KEY,
	Trucktype VARCHAR(50) NOT NULL
);
-- Create tables DimStation  --
CREATE TABLE DimStation(
	Stationid INT NOT NULL PRIMARY KEY,
	City VARCHAR(50) NOT NULL
);
-- Create tables FactTrips  --
CREATE TABLE FactTrips (
	Tripid INT NOT NULL PRIMARY KEY,
	Dateid INT NOT NULL,
	Stationid INT NOT NULL,
	Truckid INT NOT NULL,
	Wastecollected DECIMAL(10,2) NOT NULL,
	FOREIGN KEY (Dateid) REFERENCES DimDate (Dateid),
	FOREIGN KEY (Stationid) REFERENCES DimStation (Stationid),
	FOREIGN KEY (Truckid) REFERENCES DimTruck (Truckid)
);