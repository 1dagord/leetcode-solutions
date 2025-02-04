"""
    [MEDIUM]
    50. Pow(x, n)

    Concepts:
    - math
    - recursion

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 16.81 MB  [Beats 100%]
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        elif n < 0:
            return 1 / self.myPow(x, -n)
        elif n % 2:
            return self.myPow(x * x, n // 2) * x
        else:
            return self.myPow(x * x, n // 2)