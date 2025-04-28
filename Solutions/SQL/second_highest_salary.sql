/*
    [MEDIUM]
    176. Second Highest Salary

    Concepts:
    - window functions

    Stats:
        Runtime | 258 ms    [Beats 94.90%]
*/

-- outer SELECT to handle
-- case of empty input
SELECT (
    SELECT
        LEAD(salary, 1) OVER (
            ORDER BY salary DESC
        ) AS income
    FROM Employee
    GROUP BY salary
    LIMIT 1
) as SecondHighestSalary