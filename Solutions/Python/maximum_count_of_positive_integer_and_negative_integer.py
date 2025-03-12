"""
    [EASY]
    2529. Maximum Count of Positive Integer and Negative Integer

    Concepts:
    - array
    - binary search

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 17.92 MB  [Beats 69.11%]
"""

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        nums = [num for num in nums if num]
        n = len(nums)

        def get_insert_position(target: int):
            l, r = 0, n - 1

            while l <= r:
                m = (l + r) // 2

                if nums[m] < target:
                    l = m + 1
                elif nums[m] > target:
                    r = m - 1
                else:
                    return m

            return l

        neg = get_insert_position(0)
        pos = get_insert_position(0.01)

        return max(neg, n - pos if pos != -1 else -1)