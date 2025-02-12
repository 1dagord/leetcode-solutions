"""
    [HARD]
    295. Find Median from Data Stream

    Concepts:
    - design
    - heap/priority queue
    - data stream

    Stats:
        Runtime | 132 ms    [Beats 68.28%]
        Memory  | 41.20 MB  [Beats 5.73%]
"""

import heapq

class MedianFinder:

    def __init__(self):
        self.max_heap = [] # smaller half
        self.min_heap = [] # larger half
        self.min_size = 0
        self.max_size = 0

    def addNum(self, num: int) -> None:
        # if even...
        if self.min_size == self.max_size:
            # pop old value off of smaller half
            # push new value to smaller half
            # push old value to larger half
            heapq.heappush(
                self.min_heap,
                -heapq.heappushpop(self.max_heap, -num)
            )
        # pop old value off of larger half
        # push new value to larger half
        # push old value to smaller half
        heapq.heappush(
            self.max_heap,
            -heappushpop(self.min_heap, num)
        )

    def findMedian(self) -> float:
        # if even...
        if self.min_size == self.max_size:
            # average values at top of both heaps
            return (self.min_heap[0] - self.max_heap[0]) / 2.0
        # if odd, return value at top of min_heap (larger half)
        return self.min_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()