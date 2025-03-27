"""
    [MEDIUM]
    2780. Minimum Index of a Valid Split

    Concepts:
    - hash table
    - sorting

    Stats:
        Runtime | 159 ms    [Beats 13.86%]
        Memory  | 34.84 MB  [Beats 9.41%]
"""

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        m = len(nums)
        dominant = sorted(nums)[m // 2]
        left, right = Counter(), Counter(nums)

        for i in range(m):
            left[nums[i]] += 1
            right[nums[i]] -= 1

            if (
                left[dominant] > (i + 1) // 2 and
                right[dominant] > (m - i - 1) // 2
            ):
                return i

        return -1