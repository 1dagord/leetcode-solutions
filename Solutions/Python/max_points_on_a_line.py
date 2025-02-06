"""
    [HARD]
    149. Max Points on a Line

    Concepts:
    - math
    - hash table

    Stats:
        Runtime | 63 ms     [Beats 33.49%]
        Memory  | 17.86 MB  [Beats 68.30%]
"""

from collections import defaultdict
from math import atan2

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        """
            For each point, calculate angle to every
            other point using inverse tangent

            Store angles in a map
            Return max number of points with same arc tangent
        """
        tangent_map = defaultdict(int)
        max_points = 1

        for p1 in points:
            tangent_map.clear()
            for p2 in points:
                # arc tan of same points is zero
                if p1 == p2:
                    continue

                (x1, y1), (x2, y2) = p1, p2

                tangent = atan2((y2 - y1), (x2 - x1))
                tangent_map[tangent] += 1

                # add 1 to include the point itself
                max_points = max(max_points, tangent_map[tangent] + 1)

        return max_points