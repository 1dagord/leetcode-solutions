"""
    [MEDIUM]
    120. Triangle

    Concepts:
    - array
    - dynamic programming

    Stats:
        Runtime | 11 ms     [Beats 18.78%]
        Memory  | 18.69 MB  [Beats 93.02%]
"""

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # memoization

        INT_MAX = 2**31 - 1
        n = len(triangle)
        memo = [[INT_MAX]*n for _ in range(n)]

        def solve(i, j) -> int:
            # if at bottom row
            if i == n - 1:
                # add value of current cell
                # adds all the way back up recursive stack
                return triangle[i][j]

            # if cell already explored
            if memo[i][j] != INT_MAX:
                return memo[i][j]

            down = triangle[i][j] + solve(i + 1, j)
            diag = triangle[i][j] + solve(i + 1, j + 1)

            # gets minimum between both choices from start
            memo[i][j] = min(down, diag)

            return memo[i][j]

        return solve(0, 0)