"""
    [EASY]
    242. Valid Anagram

    Concepts:
    - string
    - hash table

    Stats:
        Runtime | 7 ms      [Beats 89.73%]
        Memory  | 17.84 MB  [Beats 64.20%]
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)