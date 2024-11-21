"""
    [EASY]
    724. Find Pivot Index

    Concepts:
    - array
    - prefix sum

    Stats:
        Runtime | 15 ms     [Beats 23.94%]
        Memory  | 17.78 MB  [Beats 42.92%]
"""

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)

        pref = [num for num in nums]
        for i in range(1, n):
            pref[i] += pref[i-1]

        pref = [0] + pref + [pref[-1]]

        for i in range(1, n + 1):
            if pref[i-1] == pref[-1] - pref[i]:
                return i - 1
        
        return -1