"""
    [EASY]
    205. Isomorphic Strings

    Concepts:
    - string
    - hash table

    Stats:
        Runtime | 9 ms      [Beats 22.87%]
        Memory  | 17.80 MB  [Beats 95.63%]
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}

        for i in range(len(s)):
            if s[i] not in s_to_t:
                s_to_t[s[i]] = t[i]
            else:
                if s_to_t[s[i]] != t[i]:
                    return False

            if t[i] not in t_to_s:
                t_to_s[t[i]] = s[i]
            else:
                if t_to_s[t[i]] != s[i]:
                    return False

        return True