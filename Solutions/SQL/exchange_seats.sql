/*
    [MEDIUM]
    626. Exchange Seats

    Concepts:
    - subqueries

    Stats:
        Runtime | 615 ms    [Beats 50.04%]
*/

SELECT
    id
    , (CASE WHEN
            id & 1 OR
                (
                    (SELECT MAX(id) FROM Seat) & 1 AND
                    id = (SELECT MAX(id) FROM Seat)
                )
        THEN COALESCE(LEAD(student, 1) OVER (ORDER BY id), student)
        ELSE COALESCE(LAG(student, 1) OVER (ORDER BY id), student)
    END) AS student
FROM Seat
