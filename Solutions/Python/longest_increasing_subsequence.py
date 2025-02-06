"""
    [MEDIUM]
    300. Longest Increasing Subsequence

    Concepts:
    - array
    - dynamic programming

    Stats:
        Runtime | 1755 ms   [Beats 53.27%]
        Memory  | 18.03 MB  [Beats 48.08%]
"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)