"""
    [MEDIUM]
    34. Find First and Last Position of Element in Sorted Array

    Concepts:
    - array
    - binary search

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 19.02 MB  [Beats 44.86%]
"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(arr: list[int], is_increasing: bool) -> int:
            l, r = 0, len(arr) - 1
            occ = -1

            while l <= r:
                m = (l + r) // 2

                if arr[m] < target:
                    l = m + 1
                elif arr[m] > target:
                    r = m - 1
                else:
                    occ = m
                    # if array is increasing...
                    if is_increasing:
                        # continue searching left
                        r = m - 1
                    else:
                        # continue searching right
                        l = m + 1

            return occ

        # search for first value
        if (first := binary_search(nums, True)) != -1:
            # search for second value
            return [first, binary_search(nums, False)]

        return [-1, -1]