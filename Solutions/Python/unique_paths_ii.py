"""
    [MEDIUM]
    63. Unique Paths II

    Concepts:
    - matrix
    - dynamic programming

    Stats:
        Runtime | 3 ms      [Beats 26.13%]
        Memory  | 18.23 MB  [Beats 7.44%]
"""

class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = defaultdict(int)

        if (m, n) == (1, 1):
            return 0 if grid[0][0] else 1

        if grid[0][0]:
            return 0

        def dfs(i, j):
            nonlocal dp

            if (i, j) == (m - 1, n - 1):
                dp[(i, j)] = 1
                return dp[(i, j)]

            if (i, j) in dp:
                return dp[(i, j)]

            if i + 1 < m and not grid[i+1][j]:
                dp[(i, j)] += dfs(i+1, j)
            if j + 1 < n and not grid[i][j+1]:
                dp[(i, j)] += dfs(i, j+1)

            return dp[(i, j)]

        return dfs(0, 0)