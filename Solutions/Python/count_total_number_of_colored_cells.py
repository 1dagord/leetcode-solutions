"""
    [MEDIUM]
    2579. Count Total Number of Colored Cells

    Concepts:
    - math

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 17.70 MB  [Beats 48.12%]
"""

class Solution:
    def coloredCells(self, n: int) -> int:
        return 1 + 4 * ((n * (n - 1)) // 2)