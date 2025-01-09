"""
    [EASY]
    28. Find the Index of the First Occurrence in a String

    Concepts:
    - string
    - string matching

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 16.35 MB  [Beats 99.95%]
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)