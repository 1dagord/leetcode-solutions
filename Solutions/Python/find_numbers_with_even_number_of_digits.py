"""
	[EASY]
	1295. Find Numbers with Even Number of Digits

	Concepts:
	- array
	- math

	Stats:
		Runtime	| 0 ms		[Beats 100%]
		Memory	| 17.90 MB	[Beats 53.99%]
"""

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if not len(str(num)) & 1:
                count += 1
        return count