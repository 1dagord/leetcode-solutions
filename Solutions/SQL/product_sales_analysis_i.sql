/*
    [MEDIUM]
    1068. Product Sales Analysis I

    Concepts:
    - joins

    Stats:
        Runtime | 1789 ms   [Beats 59.26%]
*/

SELECT product_name, year, price
FROM Sales AS s
LEFT JOIN Product AS p
ON s.product_id = p.product_id