"""
    [MEDIUM]
    97. Interleaving String

    Concepts:
    - string
    - dynamic programming

    Stats:
        Runtime | 46 ms     [Beats 51.92%]
        Memory  | 19.39 MB  [Beats 5.85%]
"""

from collections import defaultdict

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)
        cache = defaultdict(bool)

        def dfs(i1, i2, string):
            nonlocal cache
            
            if (i1, i2) in cache:
                return cache[(i1, i2)]
            
            if i1 == n1 and i2 == n2:
                return string == s3

            # recurse if either string has next character
            if i1 < n1 and i1 + i2 < n3 and s1[i1] == s3[i1+i2]:
                cache[(i1, i2)] |= dfs(i1+1, i2, string + s1[i1])
            if i2 < n2 and i1 + i2 < n3 and s2[i2] == s3[i1+i2]:
                cache[(i1, i2)] |= dfs(i1, i2+1, string + s2[i2])

            return cache[(i1, i2)]

        return dfs(0, 0, "")