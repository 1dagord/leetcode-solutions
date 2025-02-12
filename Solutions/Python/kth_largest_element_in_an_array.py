"""
    [MEDIUM]
    215. Kth Largest Element in an Array

    Concepts:
    - array
    - heap/priority queue

    Stats:
        Runtime | 101 ms    [Beats 27.28%]
        Memory  | 26.60 MB  [Beats 99.01%]
"""

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums_left = max(0, min(n - k, n))
        heapq.heapify(nums)
        
        while nums and nums_left:
            heapq.heappop(nums)
            nums_left -= 1

        return heapq.heappop(nums)
        
