"""
    [MEDIUM]
    2560. House Robber IV

    Concepts:
    - array
    - binary search

    Stats:
        Runtime | 287 ms    [Beats 70.38%]
        Memory  | 28.62 MB  [Beats 50.00%]
"""

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        """
            Same pattern as "Koko Eating Bananas"
            Binary search on a *range* of values
        """
        # set bounds of BS to min and max possible capability
        l, r = min(nums), max(nums)
        n = len(nums)
        res = r

        def is_valid(capability: int) -> bool:
            """
                Returns True if given minimum capability
                `capability`, robber can rob
                at least k houses
            """
            i = 0
            count = 0

            while i < n:
                if nums[i] <= capability:
                    i += 2
                    count += 1
                else:
                    i += 1

                if count == k:
                    break

            return count == k

        while l <= r:
            m = (l + r) // 2

            # if robber can rob >= k houses
            # given `m` capability...
            if is_valid(m):
                res = m
                r = m - 1
            else:
                l = m + 1

        return res