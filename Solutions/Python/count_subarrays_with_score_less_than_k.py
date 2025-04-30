"""
	[HARD]
	2302. Count Subarrays With Score Less Than K

	Concepts:
	- sliding window
	- prefix sum

	Stats:
		Runtime	| 111 ms	[Beats 82.08%]
		Memory	| 30.70 MB	[Beats 30.80%]
"""

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        """
            Since array values are all non-negative,
            any subarray sum is monotonically increasing

            When using two pointers, shifting in left pointer
            while right is fixed results in a monotonically
            decreasing subarray score

            Thus, if a subarray is valid, all subarrays created
            by shifting its left pointer are also valid
        """
        n = len(nums)
        count = 0

        pref_sum = 0

        left = 0
        for right in range(n):
            pref_sum += nums[right]

            while (
                left <= right and
                pref_sum * (right - left + 1) >= k
            ):
                pref_sum -= nums[left]
                left += 1

            count += right - left + 1

        return count