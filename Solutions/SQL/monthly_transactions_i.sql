/*
    [MEDIUM]
    1193. Monthly Transactions I

    Concepts:
    - aggregate functions

    Stats:
        Runtime | 729 ms    [Beats 73.05%]
*/

SELECT
    CONCAT(
        YEAR(trans_date), "-", LPAD(MONTH(trans_date), 2, "0")
    ) AS month
    , country
    , COUNT(id) AS trans_count
    , SUM(CASE state WHEN state="approved" THEN 1 ELSE 0 END) AS approved_count
    , SUM(amount) AS trans_total_amount
    , SUM(CASE state WHEN state="approved" THEN amount ELSE 0 END) AS approved_total_amount
FROM Transactions
GROUP BY country, month