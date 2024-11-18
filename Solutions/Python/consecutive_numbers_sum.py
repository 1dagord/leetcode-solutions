"""
    [HARD]
    829. Consecutive Numbers Sum

    Concepts:
    - math
    - enumeration

    Stats:
        Runtime | 159 ms    [Beats 16.37%]
        Memory  | 16.5 MB   [Beats 93.47%]
"""

class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        """
            Sum of all integers in range [1, n]:
            (n * (n + 1)) / 2

            There are i integers between k and n, inclusive

            N = k + (k + 1) + ... + (k + (i - 1))
            => N = k * (0 + 1 + ... + (i - 1))
            => N = ((i * k) + (i * (i - 1))) / 2
            => N - ((i - 1) * 2) / 2 = i * k

            As long as N - ((i - 1) * 2) / 2 is divisible
            by i, solution will correspond to i
        """
        count = 0

        i = 1
        while (i * (i - 1)) / 2 < n:
            if (n - (i * (i - 1) / 2)) % i == 0:
                count += 1
            i += 1
        return count