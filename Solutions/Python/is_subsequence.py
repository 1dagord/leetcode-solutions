"""
    [EASY]
    392. Is Subsequence

    Concepts:
    - string
    - two pointers

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 16.68 MB  [Beats 100%]
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_ptr = 0
        t_ptr = 0

        len_s = len(s)
        len_t = len(t)

        while s_ptr < len_s and t_ptr < len_t:
            if t[t_ptr] == s[s_ptr]:
                s_ptr += 1
            t_ptr += 1

        return s_ptr == len_s