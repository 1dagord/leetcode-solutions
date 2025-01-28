/*
    [EASY]
    596. Classes More Than 5 Students

    Concepts:
    - sorting/grouping

    Stats:
        Runtime | 367 ms    [Beats 77.42%]
*/

SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(student) >= 5