"""
    [MEDIUM]
    72. Edit Distance

    Concepts:
    - string
    - dynamic programming

    Stats:
        Runtime | 63 ms     [Beats 64.56%]
        Memory  | 21.18 MB  [Beats 57.98%]
"""

class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        """
            Imagine 2D matrix where chars of word1
            are along column and chars of word2 are
            along rows
        """
        m, n = len(w1), len(w2) 
        dp = [[float("inf")]*(n+1) for _ in range(m+1)]

        # initialize empty rows and cols for case
        # when either string is empty
        for j in range(n + 1):
            dp[m][j] = n - j
        for i in range(m + 1):
            dp[i][n] = m - i

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if w1[i] == w2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i+1][j],     # delete
                        dp[i][j+1],     # insert
                        dp[i+1][j+1]    # replace
                    )

        return dp[0][0]