/*
    [EASY]
    584. Find Customer Referee

    Concepts:
    - select

    Stats:
        Runtime | 623 ms    [Beats 64.26%]
*/

SELECT name
FROM Customer
WHERE referee_id != 2
    OR referee_id IS NULL