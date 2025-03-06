"""
    [EASY]
    219. Contains Duplicate II

    Concepts:
    - array
    - hash table

    Stats:
        Runtime | 20 ms     [Beats 65.61%]
        Memory  | 29.91 MB  [Beats 69.87%]
"""

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        idx = {}
        for i in range(len(nums)):
            if nums[i] in idx and abs(i - idx[nums[i]]) <= k:
                return True
            idx[nums[i]] = i

        return False