/*
    [MEDIUM]
    1204. Last Person to Fit in the Bus

    Concepts:
    - select
    - joins

    Stats:
        Runtime | 1355 ms   [Beats 63.06%]
*/

WITH RunningTotal AS (
    SELECT
        person_id
        , SUM(weight) OVER (ORDER BY turn) AS run_total
    FROM Queue
)
SELECT
    person_name
FROM Queue q
LEFT JOIN RunningTotal r
    ON q.person_id = r.person_id
WHERE run_total <= 1000
ORDER BY turn DESC
LIMIT 1
