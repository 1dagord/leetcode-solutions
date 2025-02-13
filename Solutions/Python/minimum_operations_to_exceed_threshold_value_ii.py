"""
    [MEDIUM]
    3066. Minimum Operations to Exceed Threshold Value II

    Concepts:
    - heap/priority queue
    - simulation

    Stats:
        Runtime | 209 ms    [Beats 73.11%]
        Memory  | 35.52 MB  [Beats 38.24%]
"""

import heapq

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0
        heapq.heapify(nums)
        while nums[0] < k:
            heapq.heappush(nums, heapq.heappop(nums) * 2 + heapq.heappop(nums)) 
            count += 1
        return count