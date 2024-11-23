"""
    [EASY]
    67. Add Binary

    Concepts:
    - bit manipulation
    - string

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 16.62 MB  [Beats 50.53%]
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]