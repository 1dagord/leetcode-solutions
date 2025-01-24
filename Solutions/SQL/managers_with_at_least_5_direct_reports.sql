/*
    [MEDIUM]
    570. Managers with at Least 5 Direct Reports

    Concepts:
    - joins

    Stats:
        Runtime | 355 ms    [Beats 84.61%]
*/

SELECT e1.name
FROM Employee e1
JOIN Employee e2
ON e1.id = e2.managerId
GROUP BY e1.id
HAVING COUNT(*) >= 5