"""
    [MEDIUM]
    3254. Find the Power of K-Size Subarrays I

    Concepts:
    - sliding window

    Stats:
        Runtime | 45 ms     [Beats 31.42%]
        Memory  | 16.7 MB   [Beats 60.96%]
"""

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        """
            Brute Force w/ Sliding Window
        """
        n = len(nums)
        res = [-1]*(n - k + 1)

        def isConsecutive(ind):
            if k == 1:
                return True

            for i in range(ind + 1, ind + k):
                if nums[i] != nums[i-1] + 1:
                    return False
            return True

        for i in range(n - k + 1):
            if isConsecutive(i):
                res[i] = nums[i+k-1]

        return res
