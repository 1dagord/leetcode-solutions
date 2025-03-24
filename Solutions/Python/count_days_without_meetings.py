"""
    [MEDIUM]
    3169. Count Days Without Meetings

    Concepts:
    - array
    - intervals

    Stats:
        Runtime | 282 ms    [Beats 10.58%]
        Memory  | 52.71 MB  [Beats 79.34%]
"""

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        prev = 0

        for s, e in meetings:
            days -= max(
                e - max(s, prev + 1) + 1
                , 0
            )
            prev = max(prev, e)

        return days