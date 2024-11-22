"""
    [HARD]
    123. Best Time to Buy and Sell Stock III

    Concepts:
    - dynamic programming
    - array

    Stats:
        Runtime | 1888 ms   [Beats 9.10%]
        Memory  | 456.84 MB [Beats 5.73%]
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
            Memoization
        """
        n = len(prices)
        dp = defaultdict(int)
        is_buying = True

        def recurse(ind, is_buying, trs):

            # if no more transactions or
            # end of prices reached, return 0
            if not trs or ind >= n:
                return 0

            if (ind, is_buying, trs) in dp:
                return dp[(ind, is_buying, trs)]
            

            # if buying...
            if is_buying:
                dp[(ind, is_buying, trs)] = max(
                    recurse(ind+1, not is_buying, trs) - prices[ind],   # buy at current price
                    recurse(ind+1, is_buying, trs)                      # or continue
                )

            # if selling...
            else:
                dp[(ind, is_buying, trs)] = max(
                    recurse(ind+1, not is_buying, trs-1) + prices[ind], # sell at current price
                    recurse(ind+1, is_buying, trs))                     # or continue


            return dp[(ind, is_buying, trs)]

        return recurse(0, is_buying, 2)
                    