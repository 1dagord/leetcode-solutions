"""
    [MEDIUM]
    1079. Letter Tile Possibilities

    Concepts:
    - string
    - backtracking

    Stats:
        Runtime | 39 ms     [Beats 57.32%]
        Memory  | 17.80 MB  [Beats 67.21%]
"""

from collections import Counter

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        counter = Counter(tiles)

        def solve():
            nonlocal counter

            total = 0

            for char in counter:
                if counter[char] > 0:
                    # remove
                    counter[char] -= 1
                    # recurse
                    total += 1 + solve()
                    # restore
                    counter[char] += 1

            return total

        return solve()