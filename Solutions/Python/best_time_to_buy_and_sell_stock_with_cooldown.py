"""
    [MEDIUM]
    309. Best Time to Buy and Sell Stock with Cooldown

    Concepts:
    - dynamic programming
    - array

    Stats:
        Runtime | 7 ms      [Beats 44.80%]
        Memory  | 18.18 MB  [Beats 28.44%]
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
            Perform DFS on decision tree

            Are we buying or are we selling?

            If buying, i += 1
            If selling, i += 2
        """
        # key: (index, isBuying)
        # value: max_profit
        cache = {}
        n = len(prices)

        def dfs(i, buying):
            # if no prices left...
            if i >= n:
                return 0

            # if index has been visited before in current state...
            if (i, buying) in cache:
                return cache[(i, buying)]

            if buying:
                # max profit after BUYING on day i
                buy = dfs(i + 1, not buying) - prices[i]
                # no state change, but index increments
                cooldown = dfs(i + 1, buying)
                # cache decision (buy or cooldown) that makes the most profit
                cache[(i, buying)] = max(buy, cooldown)

            else:
                # max profit after SELLING on day i
                sell = dfs(i + 2, not buying) + prices[i]
                # no state change, but index increments
                cooldown = dfs(i + 1, buying)
                # cache decision (sell or cooldown) that makes the most profit
                cache[(i, buying)] = max(sell, cooldown)

            return cache[(i, buying)]

        return dfs(0, True)