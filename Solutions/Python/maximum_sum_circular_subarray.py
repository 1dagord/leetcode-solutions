"""
    [MEDIUM]
    918. Maximum Sum Circular Subarray

    Concepts:
    - array
    - kadane's algorithm

    Stats:
        Runtime | 92 ms     [Beats 77.21%]
        Memory  | 21.34 MB  [Beats 50.59%]
"""

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr_max, curr_min = 0, 0
        max_sum, min_sum = -float("inf"), float("inf")

        for num in nums:
            curr_max = max(curr_max + num, num)
            curr_min = min(curr_min + num, num)
            max_sum = max(curr_max, max_sum)
            min_sum = min(curr_min, min_sum)

        return (
            max(max_sum, sum(nums) - min_sum)
            if max_sum > 0
            else max_sum
        )