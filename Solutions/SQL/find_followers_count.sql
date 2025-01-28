/*
    [EASY]
    1729. Find Followers Count

    Concepts:
    - sorting/grouping

    Stats:
        Runtime | 1037 ms   [Beats 34.76%]
*/

SELECT
    user_id
    , COUNT(follower_id) AS followers_count
FROM Followers
GROUP BY user_id
ORDER BY user_id