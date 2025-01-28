/*
    [EASY]
    1789. Primary Department for Each Employee

    Concepts:
    - select
    - sorting/grouping

    Stats:
        Runtime | 838 ms    [Beats 56.89%]
*/

WITH Singles AS (
    SELECT employee_id
    FROM Employee
    GROUP BY employee_id
    HAVING COUNT(department_id) = 1
)
SELECT
    employee_id, department_id
FROM Employee
WHERE primary_flag = "Y" OR (
    employee_id IN (
        SELECT *
        FROM Singles
    )
)
GROUP BY employee_id