"""
	[MEDIUM]
	2845. Count of Interesting Subarrays

	Concepts:
	- array
	- prefix sum

	Stats:
		Runtime	| 167 ms 	[Beats 45.71%]
		Memory	| 47.73 MB	[Beats 45.14%]
"""

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        n = len(nums)
        total = 0 # total number of interesting subarrays
        valid = 0 # number of indices satisfying condition
        freq = defaultdict(int) # mod_value |-> frequency
        freq[0] = 1 # base case: 0 mod, 1 occurrance

        for i in range(n):
            valid += (nums[i] % modulo == k)

            # current mod value
            mod = valid % modulo
            # current prefix mod
            target = (mod - k % modulo) % modulo

            # add count of occurrences of prefix mod
            total += freq[target]
            # update occurrances of current mod value
            freq[mod] += 1

        return total