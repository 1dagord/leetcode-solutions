"""
    [MEDIUM]
    57. Insert Interval

    Concepts:
    - array

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 19.76 MB  [Beats 41.64%]
"""

class Solution:
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        intervals.append(new_interval)
        intervals.sort()

        res = []

        for i in range(len(intervals)):
            # compare last interval's end with current interval's *start*
            if res and res[-1][1] >= intervals[i][0]:
                # # compare last interval's end with current interval's *end*
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                # if no overlap between last and current, create new interval
                res.append(intervals[i])

        return res