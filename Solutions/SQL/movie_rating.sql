/*
    [MEDIUM]
    1341. Movie Rating

    Concepts:
    - subqueries

    Stats:
        Runtime | 2188 ms   [Beats 49.80%]
*/

(
    SELECT u.name AS results
    FROM Users u
    JOIN MovieRating mr USING (user_id)
    GROUP BY mr.user_id
    ORDER BY COUNT(mr.user_id) DESC, u.name ASC
    LIMIT 1
)
UNION ALL
(
    SELECT m.title
    FROM MovieRating mr
    JOIN Movies m USING (movie_id)
    WHERE mr.created_at BETWEEN "2020-02-01" AND "2020-02-29"
    GROUP BY m.title
    ORDER BY AVG(mr.rating) DESC, m.title ASC
    LIMIT 1
)