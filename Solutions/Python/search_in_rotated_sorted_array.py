"""
    [MEDIUM]
    33. Search in Rotated Sorted Array

    Concepts:
    - binary search
    - array

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 16.9 MB   [Beats 89.27%]
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
            Divide array into strictly increasing part and pivoted part
            Decide which part target is in
            Run Binary Search on that part
        """
        n = len(nums)
        left  = 0
        right = n - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            # if left half is sorted...
            if nums[left] <= nums[mid]:
                # and target is inside sorted left half...
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            
        return -1