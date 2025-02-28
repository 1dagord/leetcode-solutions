"""
    [HARD]
    1092. Shortest Common Supersequence

    Concepts:
    - string
    - dynamic programming

    Stats:
        Runtime | 346 ms    [Beats 97.57%]
        Memory  | 42.48 MB  [Beats 91.78%]
"""

class Solution:
    def shortestCommonSupersequence(self, s1: str, s2: str) -> str:
        m, n = len(s1), len(s2)
        dp = [[0]*(n+1) for _ in range(m+1)]

        # find longest common subsequence
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])

        i, j = 0, 0
        res = ""

        while i < m and j < n:
            # if subsequences are same length...
            if s1[i] == s2[j]:
                res += s1[i]
                i += 1
                j += 1
            # if sequence in next row is shorter...
            elif dp[i+1][j] > dp[i][j+1]:
                res += s1[i]
                i += 1
            # if sequence in next col is shorter...
            else:
                res += s2[j]
                j += 1

        # append any leftover characters
        if i < m:
            res += s1[i:]
        if j < n:
            res += s2[j:]

        return res