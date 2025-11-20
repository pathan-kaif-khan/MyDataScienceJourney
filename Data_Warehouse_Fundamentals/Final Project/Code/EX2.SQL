--  Create MyDimDate Table  --
CREATE TABLE MyDimDate (
	Dateid INT NOT NULL PRIMARY KEY,
	Date DATE NOT NULL,
	Year INT NOT NULL,
	Quarter INT NOT NULL,
	QuarterName VARCHAR(50) NOT NULL,
	Month INT NOT NULL,
	Monthname VARCHAR(50) NOT NULL,
	Weekday INT NOT NULL,
	WeekdayName VARCHAR(50) NOT NULL
);
--  Create MyDimWaste Table  --
CREATE TABLE MyDimWaste(
	Wasteid INT NOT NULL PRIMARY KEY,
	Wastetype VARCHAR(50) NOT NULL
);
--  Create MyDimZone Table  --
CREATE TABLE MyDimZone (
	Zoneid INT NOT NULL PRIMARY KEY,
	Collectionzone VARCHAR(50) NOT NULL,
	City VARCHAR(50) NOT NULL
);
--  Create MyFactTrips  --
CREATE TABLE MyFactTrips(
	Tripid INT NOT NULL PRIMARY KEY,
	Dateid INT NOT NULL,
	Wasteid INT NOT NULL,
	Zoneid INT NOT NULL,
	Wastecollectedton DECIMAL(10,2) NOT NULL,
	FOREIGN KEY (Dateid) REFERENCES MyDimDate (Dateid),
	FOREIGN KEY (Wasteid) REFERENCES MyDimWaste (Wasteid),
	FOREIGN KEY (Zoneid) REFERENCES MyDimZone (Zoneid)
);