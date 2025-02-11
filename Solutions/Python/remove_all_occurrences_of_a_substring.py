"""
    [MEDIUM]
    1910. Remove All Occurrences of a Substring

    Concepts:
    - string

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 17.91 MB  [Beats 32.79%]
"""

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        n = len(part)
        while (idx := s.find(part)) != -1:
            s = s[:idx] + s[idx+n:]
        return s