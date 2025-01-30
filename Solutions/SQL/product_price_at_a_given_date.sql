/*
    [MEDIUM]
    1164. Product Price at a Given Date

    Concepts:
    - select
    - joins

    Stats:
        Runtime | 659 ms    [Beats 73.29%]
*/

SELECT
    p1.product_id
    , IF (
        -- if first change date before date in question...
        MIN(p1.change_date) <= "2019-08-16"
        -- execute when true
        , (
            -- select max price...
            SELECT MAX(p2.new_price)
            FROM Products p2
            WHERE
                -- where change date is in table of...
                p1.product_id = p2.product_id
                    AND (p2.product_id, change_date) IN (
                        -- products with change date before target
                        SELECT product_id, MAX(change_date)
                        FROM Products
                        WHERE change_date <= "2019-08-16" 
                        GROUP BY product_id
                    )
            GROUP BY p2.product_id
        )
        -- execute when false
        , 10
    ) AS price
FROM Products p1
GROUP BY p1.product_id