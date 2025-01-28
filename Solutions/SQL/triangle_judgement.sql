/*
    [EASY]
    610. Triangle Judgement

    Concepts:
    - select

    Stats:
        Runtime | 417 ms    [Beats 55.30%]
*/

SELECT
    x, y, z
    , IF(
        (
            x + y > z
                AND y + z > x
                AND z + x > y
        )
        , "Yes"
        , "No"
    ) AS triangle
FROM Triangle