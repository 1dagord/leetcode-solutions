"""
    [EASY]
    1790. Check if One String Swap Can Make Strings Equal

    Concepts:
    - string
    - hash table

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 17.78 MB  [Beats 47.15%]
"""

from collections import Counter

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        swappable = {}
        swap_count = 0

        if Counter(s1) != Counter(s2):
            return False

        for i, (c1, c2) in enumerate(zip(s1, s2)):
            if c1 != c2:
               swappable[c1] = c2
               swappable[c2] = c1
               swap_count += 1
            if swap_count > 2:
                return False

        return all([v in swappable for v in swappable.values()])