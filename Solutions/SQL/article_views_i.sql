/*
    [EASY]
    1148. Article Views I

    Concepts:
    - select
    - sorting/grouping

    Stats:
        Runtime | 584 ms    [Beats 60.93%]
*/

SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
GROUP BY author_id
ORDER BY author_id