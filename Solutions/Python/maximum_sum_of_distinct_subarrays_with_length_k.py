"""
    [MEDIUM]
    2461. Maximum Sum of Distinct Subarrays With Length K

    Concepts:
    - sliding window
    - hash table

    Stats:
        Runtime | 97 ms     [Beats 84.63%]
        Memory  | 36.42 MB  [Beats 22.43%]
"""

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        """
            Sliding Window
        """
        n = len(nums)
        max_sum = 0
        curr_sum = 0
        seen = {}

        for i in range(n):
            # update `seen` and `curr_sum`
            right = nums[i]

            if right in seen:
                seen[right] += 1
            else:
                seen[nums[i]] = 1
                
            curr_sum += nums[i]

            # slide window if true
            if i >= k:
                left = nums[i-k]
                seen[left] -= 1
                curr_sum -= left

                if not seen[left]:
                    del seen[left]

            # check if distinct
            if len(seen) == k:
                max_sum = max(curr_sum, max_sum)
        
        return max_sum