"""
    [MEDIUM]
    189. Rotate Array

    Concepts:
    - array
    - math

    Stats:
        Runtime | 5 ms      [Beats 53.43%]
        Memory  | 25.62 MB  [Beats 32.20%]
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        
        cpy = nums.copy()

        for i, num in enumerate(cpy):
            nums[i] = cpy[(i - k) % n]
        