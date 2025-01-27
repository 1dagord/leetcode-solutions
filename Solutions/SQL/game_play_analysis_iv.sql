/*
    [MEDIUM]
    550. Game Play Analysis IV

    Concepts:
    - aggregate functions

    Stats:
        Runtime | 968 ms    [Beats 49.17%]
*/

SELECT
    ROUND(
        COUNT(player_id) / (
            SELECT COUNT(DISTINCT player_id)
            FROM Activity
        )
        , 2
    ) AS fraction
FROM Activity
WHERE (player_id, ADDDATE(event_date, -1)) IN (
    SELECT player_id, MIN(event_date)
    FROM Activity
    GROUP BY player_id
)