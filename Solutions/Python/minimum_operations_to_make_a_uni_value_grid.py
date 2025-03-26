"""
    [MEDIUM]
    2033. Minimum Operations to Make a Uni-Value Grid

    Concepts:
    - array
    - math

    Stats:
        Runtime | 192 ms    [Beats 38.16%]
        Memory  | 39.28 MB  [Beats 36.40%]
"""

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        values = sorted([val for row in grid for val in row])
        n = len(values)

        if n == 1:
            return 0

        if not all([val % x == values[0] % x for val in values]):
            return -1

        return sum([abs(values[n // 2] - val) // x for val in values])