"""
    [EASY]
    121. Best Time to Buy and Sell Stock

    Concepts:
    - array

    Stats:
        Runtime | 29 ms     [Beats 88.06%]
        Memory  | 25.86 MB  [Beats 96.90%]
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = 10**8 + 1

        for price in prices:
            if price < min_price:
                min_price = price
            if (revenue := price - min_price) > max_profit:
                max_profit = revenue

        return max_profit