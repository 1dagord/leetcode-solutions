"""
    [EASY]
    88. Merge Sorted Array

    Concepts:
    - two pointers
    - sorting

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 16.74 MB  [Beats 87.30%]
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr = 0
        while len(nums1) > m and nums1[-1] == 0:
            nums1.pop(-1)

        while nums2:
            val = nums2[0]
            while ptr < len(nums1) and nums1[ptr] < val:
                ptr += 1
            nums1.insert(ptr, val)
            nums2 = nums2[1:]
