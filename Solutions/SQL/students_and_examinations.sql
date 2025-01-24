/*
    [EASY]
    1280. Students and Examinations

    Concepts:
    - joins

    Stats:
        Runtime | 1863 ms   [Beats 23.51%]
*/

SELECT
    stu.student_id
    , student_name
    , sub.subject_name
    , COUNT(e.student_id) AS attended_exams
FROM Students AS stu
JOIN Subjects AS sub
LEFT JOIN Examinations AS e
ON e.subject_name = sub.subject_name
    AND e.student_id = stu.student_id
GROUP BY stu.student_name, sub.subject_name
ORDER BY stu.student_id, sub.subject_name