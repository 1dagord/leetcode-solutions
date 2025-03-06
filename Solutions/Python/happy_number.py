"""
    [EASY]
    202. Happy Number

    Concepts:
    - math
    - hash table

    Stats:
        Runtime | 3 ms      [Beats 42.10%]
        Memory  | 16.60 MB  [Beats 100%]
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set([n])

        while n != 1:
            nums = [d for d in str(n)]
            nums = [int(d)**2 for d in nums]
            n = sum(nums)

            if n in visited:
                return False
            visited.add(n)

        return True