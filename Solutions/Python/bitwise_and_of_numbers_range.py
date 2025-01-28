"""
    [MEDIUM]
    201. Bitwise AND of Numbers Range

    Concepts:
    - bit manipulation

    Stats:
        Runtime | 11 ms     [Beats 19.59%]
        Memory  | 17.62 MB  [Beats 62.00%]
"""

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        """
            For every set number represented by a
            single set bit, if 1 - number is in range,
            that bit must be reset in the answer
        """

        while right > left:
            right &= (right - 1)

        return right