/*
    [EASY]
    1633. Percentage of Users Attended a Contest

    Concepts:
    - aggregate functions

    Stats:
        Runtime | 1129 ms   [Beats 76.03%]
*/

SELECT
    contest_id
    , ROUND(
            COUNT(user_id) * 100
            / (SELECT COUNT(*) FROM Users)
        , 2) AS percentage
FROM Register
GROUP BY contest_id
ORDER BY percentage DESC, contest_id