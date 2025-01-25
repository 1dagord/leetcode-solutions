"""
    [HARD]
    135. Candy

    Concepts:
    - array
    - greedy

    Stats:
        Runtime | 21 ms     [Beats 23.11%]
        Memory  | 18.98 MB  [Beats 100%]
"""

class Solution:
    def candy(self, ratings: List[int]) -> int:
        # if adjacent indices, higher gets more candy
        n = len(ratings)
        candies = [1]*n

        # forward pass
        # if rating higher than LH neighbor, increment
        for i in range(1, n):
            lhn, rhn = ratings[i-1:i+1]
            if (lhn < rhn):
                candies[i] = (1 + candies[i-1])

        # backward pass
        # if rating higher than RH neighbor, increment
        for i in range(n-2, -1, -1):
            lhn, rhn = ratings[i:i+2]
            if (lhn > rhn):
                candies[i] = max(candies[i], 1 + candies[i+1])
                
        return sum(candies)