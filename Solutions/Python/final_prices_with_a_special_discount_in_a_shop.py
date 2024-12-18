"""
    [EASY]
    1475. Final Prices With a Special Discount in a Shop

    Concepts:
    - array

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 17.96 MB  [Beats 10.80%]
"""

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        discounts = [-1]*n

        for i in range(n):
            for j in range(i+1, n):
                if prices[j] <= prices[i]:
                    discounts[i] = prices[j]
                    break

        res = [(prices[i] - discounts[i]
                if discounts[i] != -1
                else prices[i])
                for i in range(n)]

        return res