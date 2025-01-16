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

            While iterating over array, each position
            offers two choices:
            
            1) extend subarray by adding current value
            2) begin new subarray at current value

            If current sum ending at previous index < 0,
            begin new subarray at current index
        """
        curr_sum, max_sum = 0, -float("inf")

        for i in range(len(nums)):
            curr_sum = max(curr_sum + nums[i], nums[i])
            max_sum = max(max_sum, curr_sum)
    
        return max_sum
