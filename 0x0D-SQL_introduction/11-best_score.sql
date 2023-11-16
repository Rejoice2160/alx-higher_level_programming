<<<<<<< HEAD
-- Lists all records in the table second_table with a score >= 10 in my MySQL server.
-- Records are ordered by descending score.
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
=======
-- Script that lists all records with a score >= 10
-- Query to lists all records with a score >= 10 in the table second_table of a database
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
>>>>>>> 0996663cd03a9b36a03118c84663faab64c4ed47
