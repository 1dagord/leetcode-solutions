"""
    [MEDIUM]
    2698. Find the Punishment Number of an Integer

    Concepts:
    - depth-first search
    - backtracking

    Stats:
        Runtime | 748 ms    [Beats 69.35%]
        Memory  | 17.75 MB  [Beats 68.75%]
"""

class Solution:
    def punishmentNumber(self, n: int) -> int:

        def dfs(s: str, target: int) -> bool:
            # if no more digits to partition...
            if not s:
                return not target

            # if target found...
            if int(s) == target:
                return True

            # recursively partition string
            for j in range(1, len(s)):
                if dfs(s[j:], target - int(s[:j])):
                    return True

            return False

        return sum([i * i for i in range(1, n + 1) if dfs(str(i * i), i)])