"""
    [MEDIUM]
    238. Product of Array Except Self

    Concepts:
    - array
    - prefix sum

    Stats:
        Runtime | 35 ms     [Beats 26.84%]
        Memory  | 26.52 MB  [Beats 14.71%]
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        pref = nums.copy()
        suff = nums.copy()

        for i in range(1, n):
            pref[i] *= pref[i-1]
            suff[n-i-1] *= suff[n-i]

        pref = [1] + pref[:-1]
        suff = suff[1:] + [1]

        return [pref[i] * suff[i] for i in range(n)]