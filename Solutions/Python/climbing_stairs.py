"""
    [EASY]
    70. Climbing Stairs

    Concepts:
    - math
    - dynamic programming

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 16.60 MB  [Beats 100%]
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {1: 1, 2: 2}
        
        def solve(n, dp):
            # return value if already found
            if n in dp:
                return dp[n]
            # use sum of previoud 2 to get next
            dp.update({n: solve(n-1, dp) + solve(n-2, dp)})

            return dp[n]
            
        return solve(n, dp)