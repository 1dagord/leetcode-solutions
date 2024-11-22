"""
    [MEDIUM]
    122. Best Time to Buy and Sell Stock II

    Concepts:
    - array
    - greedy

    Stats:
        Runtime | 4 ms      [Beats 19.24%]
        Memory  | 17.61 MB  [Beats 83.81%]
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy as soon as price drops
        # sell as soon as price rises
        max_profit = 0
        yesterday = prices[0]

        for i in range(len(prices)):
            today = prices[i]
            # if true, sell stock
            if yesterday < today:
                max_profit += prices[i] - yesterday

            yesterday = prices[i]

        return max_profit