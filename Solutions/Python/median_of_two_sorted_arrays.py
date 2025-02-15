"""
    [HARD]
    4. Median of Two Sorted Arrays

    Concepts:
    - sorting
    - binary search

    Stats:
        Runtime | 9 ms      [Beats 8.43%]
        Memory  | 18.05 MB  [Beats 59.73%]
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        l, r = 0, m
        inf = float("inf")

        while l <= r:
            part1 = (l + r) // 2
            part2 = (m + n + 1) // 2 - part1

            max_left_1 = -inf if part1 == 0 else nums1[part1 - 1]
            min_right_1 = inf if part1 == m else nums1[part1]
            max_left_2 = -inf if part2 == 0 else nums2[part2 - 1]
            min_right_2 = inf if part2 == n else nums2[part2]

            if max_left_1 <= min_right_2 and max_left_2 <= min_right_1:
                if (m + n) & 1:
                    return max(max_left_1, max_left_2)
                return (
                    max(max_left_1, max_left_2)
                    + min(min_right_1, min_right_2)
                ) / 2

            elif max_left_1 > min_right_2:
                r = part1 - 1
            else:
                l = part1 + 1

        return -1