"""
    [EASY]
    69. Sqrt(x)

    Concepts:
    - math
    - binary search

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 17.72 MB  [Beats 46.08%]
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x

        while l <= r:
            m = (l + r) // 2

            if m * m < x:
                l = m + 1
            elif m * m > x:
                r = m - 1
            else:
                return m

        return r