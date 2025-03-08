"""
    [MEDIUM]
    221. Maximal Square

    Concepts:
    - matrix
    - dynamic programming

    Stats:
        Runtime | 163 ms    [Beats 39.08%]
        Memory  | 34.51 MB  [Beats 17.57%]
"""

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[int(val) for val in row] + [0] for row in matrix]
        dp.append([0]*(n+1))

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                neighbors = [
                    dp[i+1][j],
                    dp[i][j+1],
                    dp[i+1][j+1]
                ]
                dp[i][j] += min(neighbors) if all(neighbors) and dp[i][j] else 0

        return max([val for row in dp for val in row]) ** 2