"""
    [MEDIUM]
    22. Generate Parentheses

    Concepts:
    - backtracking
    - depth-first search

    Stats:
        Runtime | 3 ms      [Beats 31.45%]
        Memory  | 17.93 MB  [Beats 59.15%]
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
            If we map each parenthesis to a move in a 
            matrix, problem becomes path enumeration from DFS
        """
        paths = []

        def dfs(i, j, path):
            if (i, j) == (n, n):
                paths.append("".join(path))

            if i <= n:
                dfs(i + 1, j, path + ["("])
            if i > j and j <= n:
                dfs(i, j + 1, path + [")"])

        dfs(0, 0, [])
        return paths