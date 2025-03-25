"""
    [MEDIUM]
    3394. Check if Grid can be Cut into Sections

    Concepts:
    - intervals
    - sorting

    Stats:
        Runtime | 397 ms    [Beats 72.30%]
        Memory  | 83.44 MB  [Beats 82.43%]
"""

class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        """
            Merge Intervals

            1) Along each axis, sort intervals by start position
            2) While iterating through sorted intervals, if there is
                a point where e1 <= s2, increment break count by 1
            3) If break count == 3, return True
        """
        sorted_x = sorted([(s, e) for s, _, e, _ in rectangles])
        sorted_y = sorted([(s, e) for _, s, _, e in rectangles])

        for intervals in [sorted_x, sorted_y]:
            lines = 0
            s1, e1 = intervals[0]

            for s2, e2 in intervals[1:]:
                if e1 <= s2:
                    lines += 1
                    # increment both pointers
                    s1, e1 = s2, e2
                else:
                    # increment only end until
                    # break in intervals reached
                    e1 = max(e1, e2)

                if lines == 2:
                    return True

        return False