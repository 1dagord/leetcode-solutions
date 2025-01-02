"""
    [EASY]
    1. Two Sum

    Concepts:
    - hash table

    Stats:
        Runtime | 5 ms      [Beats 38.78%]
        Memory  | 19.80 MB  [Beats 7.23%]
"""

from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        items = defaultdict(list)

        for i, num in enumerate(nums):
            items[num].append(i)

        for i, num in enumerate(nums):
            if target - num in items:
                for j in items[target - num]:
                    if i != j:
                        return [i, j]