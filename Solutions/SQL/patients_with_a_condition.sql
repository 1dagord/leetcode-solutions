/*
    [EASY]
    1527. Patients With a Condition

    Concepts:
    - string
    - regex

    Stats:
        Runtime | 388 ms    [Beats 60.57%]
*/

SELECT *
FROM Patients
WHERE conditions REGEXP '^DIAB1| DIAB1'