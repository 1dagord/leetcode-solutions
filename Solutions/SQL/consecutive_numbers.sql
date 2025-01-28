/*
    [MEDIUM]
    180. Consecutive Numbers

    Concepts:
    - select
    - joins

    Stats:
        Runtime | 845 ms    [Beats 58.81%]
*/

SELECT DISTINCT
    num AS ConsecutiveNums
FROM (
    SELECT 
        LAG(num, 1) OVER (ORDER BY id) AS pre
        , num
        , LEAD(num, 1) OVER (ORDER BY id) AS nxt
    FROM Logs
) AS ConsecutiveNums
WHERE pre = num AND num = nxt