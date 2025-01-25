"""
    [EASY]
    13. Roman to Integer

    Concepts:
    - string
    - hash table

    Stats:
        Runtime | 5 ms      [Beats 53.91%]
        Memory  | 16.72 MB  [Beats 99.99%]
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        r_to_i = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        n = len(s)
        num = 0
        i = 0
        while i < n:
            cur = s[i]
            if i < n - 1 and r_to_i[cur] < r_to_i[(nxt := s[i+1])]:
                num += r_to_i[nxt] - r_to_i[cur]
                i += 1
            else:
                num += r_to_i[cur]

            i += 1

        return num
                