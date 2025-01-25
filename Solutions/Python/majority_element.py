"""
    [EASY]
    169. Majority Element

    Concepts:
    - array
    - counting

    Stats:
        Runtime | 3 ms      [Beats 82.86%]
        Memory  | 19.54 MB  [Beats 13.58%]
"""

from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return Counter(nums).most_common(1)[0][0]