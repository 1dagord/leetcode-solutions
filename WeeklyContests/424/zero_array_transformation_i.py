"""
    [MEDIUM]
    3355. Zero Array Transformation I

    Concepts:
    - array

    Stats:
        Runtime | 90 ms     [Beats 100%]
        Memory  | 55.1 MB   [Beats 100%]
"""

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        """ 
            Difference Array Techinque

            Leverage a prefix sum to process all queries
            and store difference between original and final values
        """
        n = len(nums)
        diff = [0]*n

        # increment begins at index l, inclusive
        # increment ends at index r, inclusive
        for l, r in queries:
            diff[l] += 1
            if r < n - 1:
                diff[r+1] -= 1

        # get prefix sum of increments
        pref = [num for num in diff]
        for i in range(1, len(pref)):
            pref[i] += pref[i-1]

        # compare max increment value with
        # nums value at each index
        for i in range(n):
            if nums[i] > pref[i]:
                return False

        return True