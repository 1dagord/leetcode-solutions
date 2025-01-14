"""
    [EASY]
    26. Remove Duplicates from Sorted Array

    Concepts:
    - array
    - two pointers

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 18.73 MB  [Beats 49.22%]
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        index = 0

        for i in range(len(nums)):
            if nums[i] not in seen:
                nums[index] = nums[i]
                seen.add(nums[i])
                index += 1

        return len(seen)