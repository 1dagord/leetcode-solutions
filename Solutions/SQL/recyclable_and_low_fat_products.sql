/*
    [EASY]
    1757. Recyclable and Low Fat Products

    Stats:
        Runtime | 1003 ms   [Beats 29.67%]
*/

SELECT product_id
FROM Products
WHERE low_fats = "Y"
AND recyclable = "Y"