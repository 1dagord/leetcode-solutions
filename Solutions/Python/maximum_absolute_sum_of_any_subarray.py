"""
    [MEDIUM]
    1749. Maximum Absolute Sum of Any Subarray

    Concepts:
    - array
    - kadane's algorithm

    Stats:
        Runtime | 60 ms     [Beats 64.96%]
        Memory  | 28.44 MB  [Beats 63.99%]
"""

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_pos_sum, max_neg_sum = -float("inf"), float("inf")
        curr_pos_sum, curr_neg_sum = 0, 0

        for num in nums:
            if curr_pos_sum < 0:
                curr_pos_sum = 0
            if curr_neg_sum > 0:
                curr_neg_sum = 0

            curr_pos_sum += num
            curr_neg_sum += num

            max_pos_sum = max(curr_pos_sum, max_pos_sum)
            max_neg_sum = min(curr_neg_sum, max_neg_sum)

        return max(abs(max_pos_sum), abs(max_neg_sum))