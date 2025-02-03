"""
    [MEDIUM]
    39. Combination Sum

    Concepts:
    - backtracking

    Stats:
        Runtime | 39 ms     [Beats 9.92%]
        Memory  | 17.98 MB  [Beats 32.81%]
"""

class Solution:
    def combinationSum(self, cands: List[int], target: int) -> List[List[int]]:
        combos = []
        cands.sort()

        def dfs(idx: int, path: list[int], curr: int):
            nonlocal combos

            if curr == target:
                combos.append(path)

            for i, num in enumerate(cands[idx:]):
                if curr < target:
                    dfs(i + idx, path + [num], curr + num)

        dfs(0, [], 0)

        return combos