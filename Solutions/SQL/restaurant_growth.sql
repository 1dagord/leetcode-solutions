/*
    [MEDIUM]
    1321. Restaurant Growth

    Concepts:
    - subqueries

    Stats:
        Runtime | 998 ms    [Beats 9.80%]
*/

WITH Totals AS (
    SELECT visited_on, SUM(amount) AS amount
    FROM Customer
    GROUP BY visited_on
), Averages AS (
    SELECT
        visited_on
        , SUM(amount) OVER (
            ORDER BY visited_on
            ROWS 6 PRECEDING
        ) AS amount
        , ROUND(
            AVG(amount) OVER (
                ORDER BY visited_on
                ROWS 6 PRECEDING
            )
            , 2
        ) AS average_amount
    FROM Totals
)
SELECT *
FROM Averages
WHERE DATEDIFF(
    visited_on
    , (SELECT MIN(visited_on) FROM Averages)
) > 5