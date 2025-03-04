/*
    [MEDIUM]
    602. Friend Requests II: Who Has the Most Friends

    Concepts:
    - subqueries

    Stats:
        Runtime | 335 ms    [Beats 91.17%]
*/

WITH AccAndReq AS (
    SELECT accepter_id AS id
    FROM RequestAccepted
    UNION ALL
    SELECT requester_id AS id
    FROM RequestAccepted 
)
SELECT id, COUNT(id) AS num
FROM AccAndReq
GROUP BY id
ORDER BY num DESC
LIMIT 1