"""
    [EASY]
    3105. Longest Strictly Increasing or Strictly Decreasing Subarray

    Concepts:
    - array

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 17.73 MB  [Beats 47.33%]
"""

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        inc, dec = 1, 1
        max_len = 1

        for i in range(1, n):
            if nums[i-1] < nums[i]:
                inc += 1
                dec = 1
            elif nums[i-1] > nums[i]:
                inc = 1
                dec += 1
            else:
                inc = 1
                dec = 1

            max_len = max(inc, dec, max_len)

        return max_len