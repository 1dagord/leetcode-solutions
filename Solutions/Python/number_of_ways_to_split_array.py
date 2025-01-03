"""
    [MEDIUM]
    2270. Number of Ways to Split Array

    Concepts:
    - array
    - prefix sum

    Stats:
        Runtime | 138 ms    [Beats 5.01%]
        Memory  | 37.94 MB  [Beats 5.01%]
"""

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0

        pref = [num for num in nums]
        suff = [num for num in nums]

        for i in range(1, n):
            pref[i] += pref[i-1]
            suff[n-i-1] += suff[n-i]

        pref = [0] + pref
        suff += [0]

        for i in range(1, n):
            if pref[i] >= suff[i]:
                count += 1

        return count