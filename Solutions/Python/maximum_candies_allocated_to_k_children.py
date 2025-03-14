"""
    [MEDIUM]
    2226. Maximum Candies Allocated to K Children

    Concepts:
    - array
    - binary search

    Stats:
        Runtime | 188 ms    [Beats 85.01%]
        Memory  | 29.65 MB  [Beats 88.94%]
"""

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        """
            For each pile, best case is when
            it can be divided evenly and all of the
            piles can be distributed among all children

            In other words, pile size = sum(candies) / k
        """
        total = sum(candies)
        if total < k:
            return 0

        l, r = 1, total // k
        pile_size = 0

        while l <= r:
            m = (l + r) // 2

            num_piles = 0
            for c in candies:
                # if pile can be distributed evenly among children...
                if c >= m:
                    # ...store number of full piles of size `r`
                    num_piles += c // m
                if num_piles >= k:
                    break

            # if more piles than children...
            if num_piles >= k:
                # ...check for larger pile size
                pile_size = m
                l = m + 1
            else:
                r = m - 1

        return pile_size