"""
    [MEDIUM]
    2799. Count Complete Subarrays in an Array

    Concepts:
    - array
    - hash table
    - sliding window

    Stats:
        Runtime | 12 ms     [Beats 66.50%]
        Memory  | 18.14 MB  [Beats 30.60%]
"""

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        num_distinct = len(set(nums))
        subarr_count = 0
        counter = defaultdict(int)
        
        left = 0
        for right in range(len(nums)):
            counter[nums[right]] += 1

            while len(counter) == num_distinct:
                counter[nums[left]] -= 1
                if not counter[nums[left]]:
                    del counter[nums[left]]

                left += 1

            subarr_count += left

        return subarr_count