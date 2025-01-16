"""
    [MEDIUM]
    64. Minimum Path Sum

    Concepts:
    - matrix
    - dynamic programming

    Stats:
        Runtime | 8 ms      [Beats 97.03%]
        Memory  | 20.16 MB  [Beats 42.36%]
"""

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[float("inf")]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                
                if i and j:
                    dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
                elif i and not j:
                    dp[i][0] = dp[i-1][0] + grid[i][0]
                elif j and not i:
                    dp[0][j] = dp[0][j-1] + grid[0][j]
                else:
                    dp[0][0] = grid[0][0]

        return dp[-1][-1]