/*
    [MEDIUM]
    1934. Confirmation Rate

    Concepts:
    - joins

    Stats:
        Runtime | 970 ms    [Beats 57.70%]
*/

SELECT
    s.user_id
    , ROUND(
        COUNT(
            CASE action
            WHEN "confirmed"
            THEN 1
            ELSE NULL
            END
        ) / COUNT(*)
        , 2
    ) AS confirmation_rate
FROM Signups s
LEFT JOIN Confirmations c
    ON s.user_id = c.user_id
GROUP BY s.user_id
ORDER BY confirmation_rate