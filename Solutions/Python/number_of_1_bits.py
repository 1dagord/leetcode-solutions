"""
    [EASY]
    191. Number of 1 Bits

    Concepts:
    - bit manipulation

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 17.70 MB  [Beats 7.15%]
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        bit_count = 0
        while n:
            if n & 1:
                bit_count += 1
            n >>= 1

        return bit_count