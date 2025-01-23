/*
    [EASY]
    1683. Invalid Tweets

    Concepts:
    - select

    Stats:
        Runtime | 785 ms    [Beats 65.29%]
*/

SELECT tweet_id
FROM Tweets
WHERE LENGTH(content) > 15