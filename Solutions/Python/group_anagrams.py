"""
    [MEDIUM]
    49. Group Anagrams

    Concepts:
    - hash table
    - string

    Stats:
        Runtime | 11 ms     [Beats 81.75%]
        Memory  | 21.11 MB  [Beats 38.90%]
"""

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        groups = defaultdict(list)

        for s in strs:
            anagram = "".join(sorted(s))
            groups[anagram].append(s)

        for a in sorted(groups):
            res.append(groups[a])

        return res