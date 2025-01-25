/*
    [EASY]
    1251. Average Selling Price

    Concepts:
    - aggregate functions

    Stats:
        Runtime | 717 ms    [Beats 93.37%]
*/

SELECT 
    p.product_id
    , IFNULL(ROUND(SUM(price * units) / SUM(units), 2), 0)
        AS average_price
FROM Prices p
LEFT JOIN UnitsSold u
ON p.product_id = u.product_id
    AND purchase_date BETWEEN start_date AND end_date
GROUP BY p.product_id