"""
    [HARD]
    188. Best Time to Buy and Sell Stock IV

    Concepts:
    - array
    - dynamic programming

    Stats:
        Runtime | 315 ms    [Beats 9.79%]
        Memory  | 84.21 MB  [Beats 7.91%]
"""

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        cache = defaultdict(int)
        n = len(prices)

        def transact(date: int, limit: int, is_buying: bool) -> int:
            nonlocal cache

            if not limit or date == n:
                return 0
            
            if (date, limit, is_buying) in cache:
                return cache[(date, limit, is_buying)]

            if is_buying:
                # either buy today or wait to buy another day
                cache[(date, limit, is_buying)] = max(
                    transact(date + 1, limit, False) - prices[date],
                    transact(date + 1, limit, True)
                )

            else:
                # either sell today or wait to sell another day
                cache[(date, limit, is_buying)] = max(
                    transact(date + 1, limit - 1, True) + prices[date],
                    transact(date + 1, limit, False)
                )

            return cache[(date, limit, is_buying)]
            
        return transact(0, k, True)