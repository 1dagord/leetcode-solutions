/*
    [EASY]
    2356. Number of Unique Subjects Taught by Each Teacher

    Concepts:
    - sorting/grouping

    Stats:
        Runtime | 906 ms    [Beats 43.34%]
*/

SELECT 
    teacher_id
    , COUNT(DISTINCT subject_id) AS cnt
FROM Teacher
GROUP BY teacher_id