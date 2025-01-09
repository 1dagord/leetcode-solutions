"""
    [MEDIUM]
    46. Permutations

    Concepts:
    - backtracking

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 18.26 MB  [Beats 5.46%]
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = []

        def backtrack(perm: list[int], remaining: set[int]):
            nonlocal perms

            if not remaining:
                perms.append(perm)

            for num in remaining:
                backtrack(perm + [num], remaining - {num})

        backtrack([], set(nums))

        return perms
            