/*
    [EASY]
    1517. Find Users With Valid E-Mails

    Concepts:
    - string
    - regex

    Stats:
        Runtime | 728 ms    [Beats 64.27%]
*/

SELECT *
FROM Users
WHERE mail REGEXP '^[A-Za-z][A-Za-z0-9\_\.\-]*@leetcode[.]com$'