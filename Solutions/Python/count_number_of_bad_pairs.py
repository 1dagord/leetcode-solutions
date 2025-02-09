"""
    [MEDIUM]
    2364. Count Number of Bad Pairs

    Concepts:
    - hash table
    - counting

    Stats:
        Runtime | 71 ms     [Beats 75.48%]
        Memory  | 38.74 MB  [Beats 82.38%]
"""

from collections import defaultdict

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        """
            j - i != nums[j] - nums[i]
            can be rewritten as
            nums[j] - j != nums[i] - i

            where each side is independent of the other

            1) Iterate over array and save pairs
            2) Store number of good pairs
                (whereever a key in pairs appeared
                more than once, add sum of
                pairs in range)
            3) Return difference between
                total and good pairs
        """
        n = len(nums)
        good_pairs = 0
        total_pairs = n * (n - 1) // 2
        pairs = defaultdict(int)

        for i in range(n):
            pairs[nums[i] - i] += 1

        for k, v in pairs.items():
            if v > 1:
                good_pairs += v * (v - 1) // 2

        return total_pairs - good_pairs