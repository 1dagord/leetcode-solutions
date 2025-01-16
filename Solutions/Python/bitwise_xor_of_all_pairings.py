"""
    [MEDIUM]
    2425. Bitwise XOR of All Pairings

    Concepts:
    - bit manipulation

    Stats:
        Runtime | 3 ms      [Beats 73.99%]
        Memory  | 36.54 MB  [Beats 48.56%]
"""

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        """
            Use following properties of XOR

            1) a ^ a = 0
            2) a ^ 0 = a
            3) (a ^ b) ^ c = a ^ (b ^ c) = a ^ b ^ b
            4) (a ^ b) ^ (a ^ c) = b ^ c

            Resulting XOR will flatten out to a long sequence of
            XORs where for length m array nums1 and
            length n array nums2, every value in nums1 will appear
            n times and every value in nums2 will appear m times.

            If either of these (m or n) is even, disregard the other array
            If both even, return 0
            If both odd, loop over both arrays
        """
        res = 0
        m, n = len(nums1), len(nums2)

        if m & 1:
            for num in nums2:
                res ^= num

        if n & 1:
            for num in nums1:
                res ^= num

        return res
