"""
    [EASY]
    1. Two Sum

    Concepts:
    - hash table

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 19.90 MB  [Beats 5.33%]
"""

from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = defaultdict(list)

        for i, num in enumerate(nums):
            seen[num].append(i)
            
            if target - num in seen and seen[target - num][0] != i:
                if num == target - num:
                    return seen[num]
                else:
                    return [seen[num][0], seen[target - num][0]]