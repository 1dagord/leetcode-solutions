"""
    [EASY]
    66. Plus One

    Concepts:
    - math

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 17.87 MB  [Beats 5.23%]
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i, digit in enumerate(digits[::-1]):
            num += digit * (10**i)

        num += 1
        res = []
        while num:
            res.append(num % 10)
            num //= 10

        return res[::-1]