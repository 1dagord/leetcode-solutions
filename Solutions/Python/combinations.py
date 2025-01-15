"""
    [MEDIUM]
    77. Combinations

    Concepts:
    - backtracking

    Stats:
        Runtime | 147 ms    [Beats 35.61%]
        Memory  | 59.60 MB  [Beats 48.60%]
"""

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(num: int, path: list[int]):
            nonlocal res

            if len(path) == k:
                res.append(path)
                return

            for i in range(num, n + 1):
                dfs(i + 1, path + [i])

        dfs(1, [])
        return res