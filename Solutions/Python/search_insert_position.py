"""
    [EASY]
    35. Search Insert Position

    Concepts:
    - array
    - binary search

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 17.12 MB  [Beats 100%]
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1

        return l