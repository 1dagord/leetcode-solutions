/*
    [EASY]
    1633. Percentage of Users Attended a Contest

    Concepts:
    - aggregate functions

    Stats:
        Runtime | 1763 ms   [Beats 38.30%]
*/

SELECT
    contest_id
    , ROUND(
            (COUNT(user_id) * 100 / (SELECT COUNT(*) FROM Users))
        , 2) AS percentage
FROM Register r
GROUP BY contest_id
ORDER BY percentage DESC, contest_id