/*
    [EASY]
    1327. List the Products Ordered in a Period

    Concepts:
    - subqueries

    Stats:
        Runtime | 724 ms    [Beats 77.69%]
*/

WITH PO AS (
    SELECT
        product_name, SUM(unit) AS unit
    FROM Products p
    JOIN Orders o
        ON p.product_id = o.product_id
    WHERE o.order_date BETWEEN
        '2020-02-01' AND '2020-02-29'
    GROUP BY product_name
)
SELECT *
FROM PO
WHERE unit > 99