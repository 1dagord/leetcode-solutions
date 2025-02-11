"""
    [MEDIUM]
    209. Minimum Size Subarray Sum

    Concepts:
    - array
    - sliding window

    Stats:
        Runtime | 8 ms      [Beats 69.48%]
        Memory  | 27.36 MB  [Beats 99.99%]
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
            1) keep track of window through two pointers
            2) grow window by incrementing right pointer
            3) if window sum exceeds target, decrease window
                size from left and continue
        """
        n = len(nums)
        min_len = n+1
        left = 0
        curr_sum = 0

        for right in range(n):
            curr_sum += nums[right]

            # if sum >= target...
            while curr_sum >= target:
                # update min_len
                if right - left + 1 < min_len:
                    min_len = right - left + 1

                # decrease sum and window size from left
                curr_sum -= nums[left]
                left += 1

        return min_len if min_len < n+1 else 0