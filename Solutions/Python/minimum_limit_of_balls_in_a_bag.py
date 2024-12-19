"""
    [MEDIUM]
    1760. Minimum Limit of Balls in a Bag

    Concepts:
    - array
    - binary search

    Stats:
        Runtime | 734 ms    [Beats 45.44%]
        Memory  | 29.53 MB  [Beats 6.86%]
"""

class Solution:
    def minimumSize(self, nums: List[int], max_ops: int) -> int:
        
        # return True if every bag can be split such that
        # no bag contains more than `max_balls` balls
        def can_split(max_balls: int) -> bool:
            ops = 0
            for num in nums:
                ops += ceil(num / max_balls) - 1
                if ops > max_ops:
                    return False

            return True

        # iterate over *range* of all values in nums
        l, r = 1, max(nums)

        # use < bc searching for minimum element
        while l < r:
            m = (l + r) // 2

            # if can split nums...
            if can_split(m):
                # update pointer and include max element
                r = m
            else:
                # update pointer and exclude min element
                l = m + 1

        # return smallest element
        return l
