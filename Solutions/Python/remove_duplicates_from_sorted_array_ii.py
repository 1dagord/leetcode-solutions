"""
    [MEDIUM]
    80. Remove Duplicates from Sorted Array II

    Concepts:
    - array
    - two pointers

    Stats:
        Runtime | 44 ms     [Beats 95.77%]
        Memory  | 16.62 MB  [Beats 99.26%]
"""

class Solution:
    def removeDuplicates(self, nums):
        if len(nums) <= 2:
            return len(nums)

        k = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1
        return k