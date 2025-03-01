"""
    [MEDIUM]
    172. Factorial Trailing Zeroes

    Concepts:
    - math

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 17.65 MB  [Beats 81.79%]
"""

class Solution:
    def trailingZeroes(self, n: int) -> int:
        """
            Legendre's Formula

            Based on an infinite sum, but we can set the upper
            bound to the one given in the problem

            https://en.wikipedia.org/wiki/Legendre%27s_formula
        """
        if not n:
            return 0

        count = 0

        i = 1
        while 5 ** i < 10 ** 4:
            count += (n // (5 ** i))
            i += 1

        return count