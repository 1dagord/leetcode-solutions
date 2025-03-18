"""
    [MEDIUM]
    2401. Longest Nice Subarray

    Concepts:
    - bit manipulation
    - sliding window

    Stats:
        Runtime | 93 ms     [Beats 52.13%]
        Memory  | 30.97 MB  [Beats 98.78%]
"""

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        longest = 1
        left = 0
        n = len(nums)
        val = 0

        for right in range(n):
            # shift in left pointer until substring valid
            while val & nums[right]:
                val ^= nums[left]
                left += 1

            # shift out right pointer
            val |= nums[right]

            longest = max(longest, right - left + 1)

        return longest