"""
    [EASY]
    290. Word Pattern

    Concepts:
    - string
    - hash table

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 16.41 MB  [Beats 100%]
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pat = list(pattern)
        string = s.split()
        p_set = set()
        s_set = set()

        if len(pat) != len(string):
            return False

        c_to_s = {}
        for p, w in zip(pat, string):
            if p not in c_to_s:
                c_to_s.update({p : w})
            else:
                if c_to_s[p] != w:
                    return False
            p_set.add(p)
            s_set.add(w)

        return len(p_set) == len(s_set)