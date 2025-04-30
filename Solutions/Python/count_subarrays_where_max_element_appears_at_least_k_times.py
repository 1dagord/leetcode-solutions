"""
	[MEDIUM]
	2962. Count Subarrays Where Max Element Appears at Least K Times

	Concepts:
	- two pointers
	- sliding window

	Stats:
		Runtime	| 103 ms 	[Beats 29.86%]
		Memory	| 29.46 MB	[Beats 90.67%]
"""

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_num = max(nums)
        count, occurrances = 0, 0

        left = 0
        for right in range(n):
            occurrances += nums[right] == max_num

            while not (occurrances < k):
                occurrances -= nums[left] == max_num
                left += 1

            count += left
        
        return count