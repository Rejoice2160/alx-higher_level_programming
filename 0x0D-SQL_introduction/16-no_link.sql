<<<<<<< HEAD
-- Lists all records of the table second_table having a name value in my MySQL server.
-- Records are ordered by descending score.
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
=======
-- Script that lists all records of a table
-- Query to lists all records of the table second_table who have name value
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
>>>>>>> 0996663cd03a9b36a03118c84663faab64c4ed47
