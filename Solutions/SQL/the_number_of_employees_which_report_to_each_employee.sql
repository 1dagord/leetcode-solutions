/*
    [EASY]
    1731. The Number of Employees Which Report to Each Employee

    Concepts:
    - select
    - joins

    Stats:
        Runtime | 1077 ms   [Beats 48.97%]
*/

SELECT
    e1.employee_id
    , e1.name
    , COUNT(e2.employee_id) AS reports_count
    , ROUND(AVG(e2.age)) AS average_age
FROM Employees e1
INNER JOIN Employees e2
    ON e2.reports_to = e1.employee_id
GROUP BY e2.reports_to
ORDER BY e1.employee_id