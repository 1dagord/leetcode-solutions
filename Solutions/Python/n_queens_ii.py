"""
    [HARD]
    52. N-Queens II

    Concepts:
    - backtracking

    Stats:
        Runtime | 7 ms      [Beats 89.33%]
        Memory  | 17.66 MB  [Beats 88.49%]
"""

class Solution:
    def totalNQueens(self, n: int) -> int:
        count = 0
        used_cols = set()
        diags = set()
        antidiags = set()

        def backtrack(i: int) -> None:
            nonlocal count

            if i == n:
                count += 1
                return

            for j in range(n):
                if j in used_cols or (i + j) in diags or (i - j) in antidiags:
                    continue

                used_cols.add(j)
                diags.add((i + j))
                antidiags.add((i - j))

                backtrack(i + 1)

                used_cols.remove(j)
                diags.remove((i + j))
                antidiags.remove((i - j))

        backtrack(0)
        return count