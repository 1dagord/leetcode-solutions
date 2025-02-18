"""
    [MEDIUM]
    2375. Construct Smallest Number From DI String

    Concepts:
    - string
    - backtracking

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 17.62 MB  [Beats 82.96%]
"""

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        res = []
        
        def backtrack(idx: int, path: list[str], used: set[int]):
            nonlocal res

            if idx == n:
                res = path
                return True
            
            for num in "123456789":
                if num in used:
                    continue

                if len(path) < 1:
                    if backtrack(idx, path + [num], used | {num}):
                        return True
                elif pattern[idx] == "I" and num > path[-1]:
                    if backtrack(idx + 1, path + [num], used | {num}):
                        return True
                elif pattern[idx] == "D" and num < path[-1]:
                    if backtrack(idx + 1, path + [num], used | {num}):
                        return True

            return False
                
        backtrack(0, [], set())
        return "".join(res)