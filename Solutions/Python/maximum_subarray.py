"""
    [MEDIUM]
    53. Maximum Subarray

    Concepts:
    - array
    - dynamic programming

    Stats:
        Runtime | 87 ms     [Beats 35.44%]
        Memory  | 32.90 MB  [Beats 13.08%]
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
            Kadane's Algorithm

            Begin constructing subarray until sum drops below
            max_sum, then begin new subarray from current position
        """
        curr_sum, max_sum = 0, -float("inf")

        for i in range(len(nums)):
            curr_sum = max(curr_sum + nums[i], nums[i])
            max_sum = max(max_sum, curr_sum)
    
        return max_sum
