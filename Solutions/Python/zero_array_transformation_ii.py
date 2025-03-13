"""
    [MEDIUM]
    3356. Zero Array Transformation II

    Concepts:
    - binary search
    - prefix sum

    Stats:
        Runtime | 612 ms    [Beats 65.46%]
        Memory  | 63.02 MB  [Beats 86.46%]
"""

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)

        if not any(nums):
            return 0

        def can_make_zero_array(k: int) -> bool:
            diff = [0]*(n+1)

            for i in range(k):
                left, right, val = queries[i]
                diff[left] += val
                diff[right+1] -= val

            curr_val = 0
            for i in range(n):
                curr_val += diff[i]
                if curr_val < nums[i]:
                    return False

            return True

        l, r = 0, len(queries)

        if not can_make_zero_array(r):
            return -1

        while l < r:
            m = (l + r) // 2

            if can_make_zero_array(m):
                r = m
            else:
                l = m + 1

        return l