/*
    [MEDIUM]
    585. Investments in 2016

    Concepts:
    - subqueries

    Stats:
        Runtime | 1331 ms   [Beats 18.54%]
*/

WITH Neighbors AS (
    SELECT i1.pid
    FROM Insurance i1
    INNER JOIN Insurance i2
    ON (
        i1.pid <> i2.pid AND
        i1.lat = i2.lat AND
        i1.lon = i2.lon
    )
), Shareholders AS (
    SELECT DISTINCT i1.pid, i1.tiv_2016
    FROM Insurance i1
    INNER JOIN Insurance i2
    ON (
        i1.pid <> i2.pid AND
        i1.tiv_2015 = i2.tiv_2015 AND
        i1.pid NOT IN (SELECT * FROM Neighbors)
    )
)
SELECT
    ROUND(
        SUM(
            tiv_2016
        )
    , 2) AS tiv_2016
FROM Shareholders