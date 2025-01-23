/*
    [EASY]
    577. Employee Bonus

    Concepts:
    - joins

    Stats:
        Runtime | 1796 ms   [Beats 31.77%]
*/

SELECT name, bonus
FROM Employee AS e
LEFT JOIN Bonus AS b
ON e.empId = b.empId
WHERE bonus < 1000 OR bonus IS NULL