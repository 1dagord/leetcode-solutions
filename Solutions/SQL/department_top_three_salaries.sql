/*
    [HARD]
    185. Department Top Three Salaries

    Concepts:
    - window functions
    - subqueries

    Stats:
        Runtime | 1106 ms   [Beats 60.54%]
*/

WITH Top3 AS (
    SELECT
        d.name AS Department
        , e.name AS Employee
        , salary AS Salary
        , DENSE_RANK() OVER (
            PARTITION BY d.name
            ORDER BY salary DESC
        ) AS row_num
    FROM Employee e
    JOIN Department d
    ON e.departmentId = d.id
)
SELECT
    Department, Employee, Salary
FROM Top3
WHERE row_num < 4