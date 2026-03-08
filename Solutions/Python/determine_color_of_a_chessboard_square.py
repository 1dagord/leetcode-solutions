"""
    [EASY]
    1812. Determine Color of a Chessboard Square

    Concepts:
    - math
    - string

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 19.14 MB  [Beats 96.71%]
"""

class Solution:
    def squareIsWhite(self, coords: str) -> bool:
        return not bool(
            ((ord("a") - ord(coords[0])) & 1)
            ^ (int(coords[1]) & 1)
        )