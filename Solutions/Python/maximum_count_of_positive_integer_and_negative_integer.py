"""
    [EASY]
    2529. Maximum Count of Positive Integer and Negative Integer

    Concepts:
    - array
    - binary search

    Stats:
        Runtime | 2 ms      [Beats 36.21%]
        Memory  | 18.08 MB  [Beats 41.77%]
"""

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        nums = list(filter(lambda num: num, nums))
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