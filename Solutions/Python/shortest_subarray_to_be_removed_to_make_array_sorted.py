"""
    [MEDIUM]
    1574. Shortest Subarray to be Removed to Make Array Sorted

    Concepts:
    - two pointers
    - prefix/suffix sum

    Stats:
        Runtime | 11 ms     [Beats 75.88%]
        Memory  | 30.3 MB   [Beats 62.13%]
"""

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)

        # find longest non-decreasing prefix
        left = 0
        for i in range(1, n):
            if arr[i] < arr[i-1]:
                break
            left += 1

        # if array already non-decreasing...
        if left == n - 1:
            return 0

        # find longest non-decreasing suffix
        right = n-1
        for i in range(n - 2, -1, -1):
            if right < left:
                break
            if arr[i] > arr[i+1]:
                break
            right -= 1

        # min elems to remove is min of removing all
        # elems right of `left` or left of `right`
        res = min(n - left - 1, right)

        # merge left and right subarrays
        i = 0
        j = right

        # pinch subarrays until not non-decreasing
        while i <= left and j < n:
            if arr[i] <= arr[j]:
                res = min(res, j - i - 1)
                i += 1
            else:
                j += 1
        return res