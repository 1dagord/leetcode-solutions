/*
    [MEDIUM]
    1378. Replace Employee ID With The Unique Identifier

    Concepts:
    - joins

    Stats:
        Runtime | 1320 ms   [Beats 73.37%]
*/

SELECT euni.unique_id, e.name
FROM EmployeeUNI as euni
RIGHT JOIN Employees AS e
ON e.id = euni.id