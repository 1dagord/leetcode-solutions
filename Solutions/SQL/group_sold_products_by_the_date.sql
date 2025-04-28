/*
    [EASY]
    1484. Group Sold Products By The Date

    Concepts:
    - string

    Stats:
        Runtime | 427 ms    [Beats 93.03%]
*/

SELECT
    sell_date
    , COUNT(DISTINCT product) AS num_sold
    , GROUP_CONCAT(DISTINCT product)
        AS products
FROM Activities
GROUP BY sell_date