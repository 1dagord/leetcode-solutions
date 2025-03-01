"""
    [EASY]
    2460. Apply Operations to an Array

    Concepts:
    - array
    - simulation

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 17.99 MB  [Beats 46.47%]
"""

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0

        res = [num for num in nums if num]
        return res + [0]*(n - len(res))