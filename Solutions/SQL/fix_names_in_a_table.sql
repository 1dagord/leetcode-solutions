/*
    [EASY]
    1667. Fix Names in a Table

    Concepts:
    - string

    Stats:
        Runtime | 626 ms    [Beats 96.19%]
*/

SELECT
    user_id
    , CONCAT(
        UPPER(
            SUBSTRING(name, 1, 1)
        )
        , LOWER(
            SUBSTRING(name, 2, CHAR_LENGTH(name) - 1)
        )
    ) AS name
FROM Users
ORDER BY user_id