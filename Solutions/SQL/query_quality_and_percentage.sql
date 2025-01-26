/*
    [EASY]
    1211. Queries Quality and Percentage

    Concepts:
    - aggregate functions

    Stats:
        Runtime | 541 ms    [Beats 59.39%]
*/

SELECT
    query_name
    , ROUND(AVG(rating / position), 2) AS quality
    , ROUND(AVG(rating < 3) * 100, 2)
        AS poor_query_percentage
FROM Queries
GROUP BY query_name;