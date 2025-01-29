/*
    [EASY]
    1581. Customer Who Visited but Did Not Make Any Transactions

    Concepts:
    - joins

    Stats:
        Runtime | 1443 ms   [Beats 76.50%]
*/

SELECT
    customer_id
    , COUNT(customer_id) AS count_no_trans
FROM Visits AS v
LEFT JOIN Transactions AS t
    ON t.visit_id = v.visit_id
WHERE transaction_id IS NULL
GROUP BY customer_id