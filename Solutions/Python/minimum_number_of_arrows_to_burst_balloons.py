"""
    [MEDIUM]
    452. Minimum Number of Arrows to Burst Balloons

    Concepts:
    - array
    - greedy
    - sorting

    Stats:
        Runtime | 83 ms     [Beats 62.73%]
        Memory  | 50.46 MB  [Beats 96.78%]
"""

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
            Find number of overlaps in ranges

            1) sort intervals by start value
            2) check if start of current interval is before
                end of previous
            3) if above is true, overlap (decrement number of arrows)
        """
        points.sort(key=lambda x: x[0])
        n = len(points)

        # max number of arrows is same as number of balloons
        arrows = n

        prev = points[0]

        for i in range(1, n):
            curr = points[i]
            s1, e1 = prev
            s2, e2 = curr

            # if overlap found, decrement number of arrows
            if s2 <= e1:
                arrows -= 1
                prev = [s2, min(e1, e2)]

            # otherwise, update previous interval
            else:
                prev = curr
        
        return arrows 