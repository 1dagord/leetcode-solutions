"""
    [MEDIUM]
    628. Maximum Product of Three Numbers

    Concepts:
    - math
    - sorting

    Stats:
        Runtime | 23 ms     [Beats 48.70%]
        Memory  | 18.95 MB  [Beats 5.75%]
"""

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        """
            Only include negative numbers if there
            are at least two

            Compare smallest negative numbers and 
            largest positive with three largest
            positive numbers
        """
        nums.sort()
        return max(
            nums[-1] * nums[-2] * nums[-3],
            nums[0] * nums[1] * nums[-1]
        )