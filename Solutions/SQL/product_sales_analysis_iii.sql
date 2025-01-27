/*
    [MEDIUM]
    1070. Product Sales Analysis III

    Concepts:
    - sorting/grouping

    Stats:
        Runtime | 1572 ms   [Beats 57.59%]
*/

SELECT
    product_id
    , year AS first_year
    , quantity
    , price
FROM Sales s
WHERE (s.product_id, s.year) IN (
    SELECT product_id, MIN(year)
    FROM Sales
    GROUP BY product_id
)