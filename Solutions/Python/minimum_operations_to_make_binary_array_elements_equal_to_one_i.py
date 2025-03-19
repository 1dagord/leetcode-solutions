"""
    [MEDIUM]
    3191. Minimum Operations to Make Binary Array Elements Equal to One I

    Concepts:
    - array
    - bit manipulation

    Stats:
        Runtime | 104 ms    [Beats 63.50%]
        Memory  | 21.56 MB  [Beats 89.20%]
"""

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        flips = 0
        n = len(nums)

        for i in range(n - 2):
            if not nums[i]:
                nums[i] ^= 1
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1
                flips += 1

        return flips if all(nums) else -1