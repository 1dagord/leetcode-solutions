"""
    [MEDIUM]
    137. Single Number II

    Concepts:
    - bit manipulation

    Stats:
        Runtime | 87 ms     [Beats 11.86%]
        Memory  | 19.16 MB  [Beats 40.13%]
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
            Use ternary representation of integer
            and implement XOR manually
        """
        ans = [0]*32

        def XOR(num1: List[int], num2: int) -> List[int]:
            res = [0]*32
            n2 = (bin(num2 & 0xFFFFFFFF))[2:].rjust(32, "0")    # big endian
            for i in range(32):
                res[i] = (num1[i] + int(n2[31 - i])) % 3
            return res

        for num in nums:
            ans = XOR(ans, num)

        res = 0
        isNegative = True if ans[-1] else False

        for i, bit in enumerate(ans):
            if (not isNegative and bit) or (isNegative and not bit):
                res |= (1 << i)
        
        if isNegative:
            return (-1 * res) - 1
        return res