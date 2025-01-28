/*
    [EASY]
    619. Biggest Single Number

    Concepts:
    - sorting/grouping

    Stats:
        Runtime | 692 ms    [Beats 43.85%]
*/

WITH Singles AS (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(num) = 1
)
SELECT MAX(num) AS num
FROM Singles