"""
    [MEDIUM]
    2054. Two Best Non-Overlapping Events

    Concepts:
    - priority queue/heap
    - intervals

    Stats:
        Runtime | 143 ms    [Beats 81.77%]
        Memory  | 57.36 MB  [Beats 61.08%]
"""

import heapq

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        """
            1) Sort events by start time
            2) Iterate over all events and store current value
            3) While current even ends before next, add value of next event
            4) Return maximum over all events
        """
        max_sum = 0
        curr_sum = 0
        pq = []
        events.sort()

        for start, end, val in events:
            # while most recent event ends before current event starts...
            while pq and pq[0][0] < start:
                # update current sum by value
                curr_sum = max(curr_sum, heapq.heappop(pq)[1])
            
            max_sum = max(max_sum, curr_sum + val)
            # push next event to heap
            heapq.heappush(pq, (end, val))

        return max_sum