"""
    [MEDIUM]
    167. Two Sum II - Input Array Is Sorted

    Concepts:
    - array
    - two pointers

    Stats:
        Runtime | 4 ms      [Beats 49.44%]
        Memory  | 17.85 MB  [Beats 100%]
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        left, right = 0, n-1
        
        min_num = nums[0]
        nums = [num + min_num for num in nums]
        target += min(nums)

        while left < right:
            if nums[left] + nums[right] > target:
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                break

        return [left + 1, right + 1]
