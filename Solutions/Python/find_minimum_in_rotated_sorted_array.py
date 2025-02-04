"""
    [MEDIUM]
    153. Find Minimum in Rotated Sorted Array

    Concepts:
    - binary search
    - array

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 17.06 MB  [Beats 6.23%]
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
            Half of array is sorted, other half is rotated

            Identify which half has min, then run Binary Search
        """
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            
            # if left > right, search right half
            if nums[l] > nums[r]:
                # if mid > left > right, search right half
                if nums[m] >= nums[l]:
                    l = m + 1
                # else, search left half
                else:
                    r = m
            else:
                return nums[l]

        return nums[r]