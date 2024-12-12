"""
    [MEDIUM]
    2779. Maximum Beauty of an Array After Applying Operation

    Concepts:
    - array
    - sliding window

    Stats:
        Runtime | 217 ms    [Beats 65.15%]
        Memory  | 28.10 MB  [Beats 39.76%]
"""

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        """
            For interval [start, end] to be valid,
            nums[end] must be within range of nums[start] +- k

            In other words,
            nums[end] - nums[start] must be <= 2*k
        """
        nums.sort()
        res, start = 0, 0

        for end in range(len(nums)):
            # if interval not eligible, increment start index
            while nums[end] - nums[start] > 2 * k:
                start += 1
            res = max(res, end - start + 1)
        
        return res