"""
    [EASY]
    2185. Counting Words With a Given Prefix

    Concepts:
    - string
    - string matching

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 17.78 MB  [Beats 27.56%]
"""

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum([int(word.startswith(pref)) for word in words])