"""
    [EASY]
    190. Reverse Bits

    Concepts:
    - bit manipulation

    Stats:
        Runtime | 27 ms     [Beats 97.25%]
        Memory  | 17.20 MB  [Beats 8.20%]
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            # if ith digit set...
            if (n & (1 << i)):
                # set same bit on other half
                res |= (1 << (31 - i))
        return res