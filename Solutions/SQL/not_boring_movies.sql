/*
    [EASY]
    620. Not Boring Movies

    Concepts:
    - aggregate functions

    Stats:
        Runtime | 373 ms    [Beats 53.71%]
*/

SELECT *
FROM Cinema
WHERE id & 1 = 1
    AND description != "boring"
ORDER BY rating DESC