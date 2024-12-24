"""
    [MEDIUM]
    128. Longest Consecutive Sequence

    Concepts:
    - array
    - hash table

    Stats:
        Runtime | 44 ms     [Beats 75.62%]
        Memory  | 34.24 MB  [Beats 19.38%]
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = 0
        vals = set(nums)

        while vals:
            val = vals.pop()

            lo, hi = val, val
            while lo - 1 in vals:
                vals.remove(lo - 1)
                lo -= 1

            while hi + 1 in vals:
                vals.remove(hi + 1)
                hi += 1

            length = max(hi - lo + 1, length)

        return length