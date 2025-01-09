"""
    [HARD]
    76. Minimum Window Substring

    Concepts:
    - sliding window
    - hash table

    Stats:
        Runtime | 62 ms     [Beats 83.72%]
        Memory  | 18.50 MB  [Beats 8.58%]
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        if m < n:
            return ""

        t_count = Counter(t)
        window = [0, float("inf")]
        start, finish = 0, n

        for end, c in enumerate(s):
            if t_count[c] > 0:
                finish -= 1

            t_count[c] -= 1

            if not finish:
                while t_count[s[start]]:
                    t_count[s[start]] += 1
                    start += 1
                if end - start < window[1] - window[0]:
                    window = [start, end]

                t_count[s[start]] += 1
                finish += 1
                start += 1

        return "" if window[1] > m else s[window[0]:window[1]+1]