/*
    [MEDIUM]
    1045. Customers Who Bought All Products

    Concepts:
    - sorting/grouping

    Stats:
        Runtime | 826 ms    [Beats 63.75%]
*/

SELECT
    customer_id
FROM Customer
GROUP BY customer_id
HAVING
    COUNT(DISTINCT product_key) = (
        SELECT COUNT(*) FROM Product
    )