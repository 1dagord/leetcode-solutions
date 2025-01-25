/*
    [EASY]
    1075. Project Employees I

    Concepts:
    - aggregate functions

    Stats:
        Runtime | 758 ms    [Beats 60.62%]
*/

SELECT project_id, ROUND(AVG(experience_years), 2)
    AS average_years
FROM Project p
LEFT JOIN Employee e
    ON p.employee_id = e.employee_id
GROUP BY project_id