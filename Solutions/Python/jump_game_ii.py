"""
    [MEDIUM]
    45. Jump Game II

    Concepts:
    - array
    - dynamic programming

    Stats:
        Runtime | 9091 ms   [Beats 5.00%]
        Memory  | 21.19 MB  [Beats 5.97%]
"""

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float("inf")]*n

        def solve(idx: int) -> bool:
            if idx >= n-1:
                return 0

            if dp[idx] != float("inf"):
                return dp[idx]

            for j in reversed(range(1, nums[idx]+1)):
                dp[idx] = min(
                    dp[idx],
                    1 + solve(idx + j)
                )

            return dp[idx]

        return solve(0)