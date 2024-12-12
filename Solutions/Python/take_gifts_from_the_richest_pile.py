"""
    [EASY]
    2558. Take Gifts From the Richest Pile

    Concepts:
    - heap/priority queue

    Stats:
        Runtime | 3 ms      [Beats 87.72%]
        Memory  | 17.39 MB  [Beats 20.60%]
"""

import heapq

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-gift for gift in gifts]
        heapq.heapify(gifts)
        while k:
            heapq.heapreplace(gifts, -floor(sqrt(-gifts[0])))
            k -= 1
        
        return -sum(gifts)
            