--  Grouping Data  --
SELECT
	FT.Stationid,
	DT.Trucktype,
	SUM(FT.Wastecollected) AS TotalWasteCollected
FROM
	FactTrips FT
JOIN
	DimTruck DT ON FT.Truckid = DT.Truckid
GROUP BY GROUPING SETS
	(FT.Stationid ,DT.Trucktype)
ORDER BY 
	FT.Stationid,
	DT.Trucktype;

--  RollUp  --
SELECT 
	DD.Year,
	DS.City,
	FT.Stationid,
	SUM(FT.Wastecollected) AS TotalWasteCollected
FROM
	FactTrips FT
JOIN 
	DimStation DS ON FT.Stationid = DS.Stationid
JOIN
	DimDate DD ON FT.Dateid = DD.Dateid
GROUP BY ROLLUP 
	(DD.Year,DS.City,FT.Stationid)
ORDER BY
	DD.Year,
	DS.City,
	FT.Stationid;

--  Cube Query  --
SELECT 
	DD.Year,
	DS.City,
	FT.Stationid,
	AVG(FT.Wastecollected) AS AvegageWasteCollected
FROM
	FactTrips FT
JOIN 
	DimStation DS ON DS.Stationid = FT.Stationid
JOIN
	DimDate DD ON DD.Dateid = FT.Dateid
GROUP BY CUBE
	(DD.Year,DS.City,FT.Stationid)
ORDER BY 
	DD.Year,
	DS.City,
	FT.Stationid;

--  Materialized View  --
CREATE MATERIALIZED VIEW max_waste_stats AS
SELECT
	DS.City,
	FT.Stationid,
	DT.Trucktype,
	MAX(FT.Wastecollected) AS MaxWasteCollected
FROM
	Facttrips FT
JOIN
	DimStation DS ON DS.Stationid = FT.Stationid
JOIN 
	DimTruck DT ON DT.Truckid = FT.Truckid
GROUP BY 
	DS.City,
	FT.Stationid,
	DT.Trucktype;

REFRESH MATERIALIZED VIEW max_waste_stats;
