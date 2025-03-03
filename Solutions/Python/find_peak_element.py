"""
    [MEDIUM]
    162. Find Peak Element

    Concepts:
    - array
    - binary search

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 17.86 MB  [Beats 61.53%]
"""

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1

        def is_peak(i: int):
            if i == 0:
                return nums[0] > nums[1] if len(nums) > 1 else True
            elif i == n-1:
                return nums[n-1] > nums[n-2]

            return nums[i-1] < nums[i] > nums[i+1]

        if r - l < 3:
            for i in range(n):
                if is_peak(i):
                    return i

        while l <= r:
            m = (l + r) // 2

            if is_peak(m):
                return m
            elif nums[m-1] > nums[m]:
                r = m - 1
            elif nums[m] < nums[m+1]:
                l = m + 1

        return l