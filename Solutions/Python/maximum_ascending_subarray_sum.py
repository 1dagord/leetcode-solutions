"""
    [EASY]
    1800. Maximum Ascending Subarray Sum

    Concepts:
    - array

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 17.75 MB  [Beats 44.25%]
"""

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n = len(nums)
        curr_sum, max_sum = 0, -float("inf")

        nums = [0] + nums

        for i in range(1, n+1):
            if nums[i-1] >= nums[i]:
                curr_sum = 0
            curr_sum += nums[i]
            max_sum = max(curr_sum, max_sum)

        return max_sum