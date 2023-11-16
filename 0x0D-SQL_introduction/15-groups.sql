<<<<<<< HEAD
-- Lists the number of records with the same score in the table second_table in my MySQL server.
-- Records are ordered by descending count.
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
=======
-- Script that lists the number of records with the same score
-- Query to lists the number of records with the same score
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY score DESC;
>>>>>>> 0996663cd03a9b36a03118c84663faab64c4ed47
