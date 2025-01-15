"""
    [MEDIUM]
    151. Reverse Words in a String

    Concepts:
    - string

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 17.80 MB  [Beats 45.94%]
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])