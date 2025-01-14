"""
    [EASY]
    27. Remove Element

    Concepts:
    - array

    Stats:
        Runtime | 0 ms      [Beast 100%]
        Memory  | 16.58 MB  [Beats 95.82%]
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ind = 0

        while ind < len(nums):
            if nums[ind] == val:
                del nums[ind]
            else:
                ind += 1

        return len(nums)
        