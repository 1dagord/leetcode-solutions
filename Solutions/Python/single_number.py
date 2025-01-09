"""
    [EASY]
    136. Single Number

    Concepts:
    - bit manipulation

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 19.62 MB  [Beats 18.92%]
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num
        return ans