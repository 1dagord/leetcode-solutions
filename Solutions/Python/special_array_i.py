"""
    [EASY]
    3151. Special Array I

    Concepts:
    - array

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 17.97 MB  [Beats 12.54%]
"""

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            if (nums[i] & 1) == (nums[i+1] & 1):
                return False
        return True