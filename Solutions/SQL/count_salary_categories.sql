/*
    [MEDIUM]
    1907. Count Salary Categories

    Concepts:
    - select
    - joins

    Stats:
        Runtime | 2739 ms   [Beats 41.65%]
*/

SELECT
    "Low Salary" AS category
    , SUM(
        CASE WHEN income < 20000
        THEN 1
        ELSE 0
        END
    ) AS accounts_count
FROM Accounts
UNION ALL
SELECT
    "Average Salary"
    , SUM(
        CASE WHEN 20000 <= income
            AND income <= 50000
        THEN 1
        ELSE 0
        END
    )
FROM Accounts
UNION ALL
SELECT
    "High Salary"
    , SUM(
        CASE WHEN 50000 < income
        THEN 1
        ELSE 0
        END
    )
FROM Accounts 