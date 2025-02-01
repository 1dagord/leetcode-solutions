/*
    [EASY]
    1978. Employees Whose Manager Left the Company

    Concepts:
    - subqueries

    Stats:
        Runtime | 557 ms    [Beats 53.83%]
*/

SELECT employee_id
FROM Employees
WHERE salary < 30000
    AND manager_id NOT IN (
        SELECT employee_id
        FROM Employees
    )
ORDER BY employee_id