"""
    [MEDIUM]
    3208. Alternating Groups II

    Concepts:
    - array
    - sliding window

    Stats:
        Runtime | 725 ms    [Beats 56.81%]
        Memory  | 21.18 MB  [Beats 90.70%]
"""

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        alt = 0
        last_same = -float("inf")
        n = len(colors)

        for i in range(1, n + k):
            if colors[(i-1) % n] == colors[i % n]:
                last_same = i-1
            else:
                if i-k >= last_same and i >= k:
                    alt += 1

        return alt