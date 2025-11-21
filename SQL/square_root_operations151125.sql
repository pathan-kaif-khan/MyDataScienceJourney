-- Create table squareroot
CREATE TABLE squareroot (
    id INT,
    num INT
);

-- Insert values into the squareroot table
INSERT INTO squareroot VALUES(4, sqrt(4));
INSERT INTO squareroot VALUES(25, sqrt(25));
INSERT INTO squareroot VALUES(49, sqrt(49));
INSERT INTO squareroot VALUES(81, sqrt(81));
INSERT INTO squareroot VALUES(16, sqrt(16));

-- Select all data from the squareroot table
SELECT  FROM squareroot;

-- Create a view to filter rows with id  20
CREATE VIEW view_sql AS
SELECT id, num
FROM squareroot
WHERE id  20;

-- Select data from the view_sql
SELECT  FROM view_sql;

-- Select all data from the squareroot table again
SELECT  FROM squareroot;

-- Delete the record where id = 25 from the squareroot table
DELETE FROM squareroot WHERE id = 25;

-- Re-insert the deleted record back into the squareroot table
INSERT INTO squareroot VALUES(25, sqrt(25));

-- Create a materialized view to filter rows with id  20
CREATE MATERIALIZED VIEW mv_sql AS
SELECT id, num
FROM squareroot
WHERE id  20;

-- Refresh the materialized view to reflect the current state of the squareroot table
REFRESH MATERIALIZED VIEW mv_sql;

-- Select data from the view_sql again
SELECT  FROM view_sql;
