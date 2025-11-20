--  Design the dimension table  --
"MyDimDate"
Dateid
Date
Year
Quarter
QuarterName
Month
Monthname
Weekday
WeekdayName

"MyDimWaste"
Wasteid
Wastetype

"MyDimZone"
Zoneid
Collectionzone
City 

"MyFactTrips"
Tripid
Dateid
Wasteid
Zoneid
Wastecollectedton
