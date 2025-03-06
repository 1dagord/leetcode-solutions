"""
    [EASY]
    383. Ransom Note

    Concepts:
    - string
    - hash table

    Stats:
        Runtime | 15 ms     [Beats 76.44%]
        Memory  | 16.80 MB  [Beats 100%]
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rCount = Counter(ransomNote)
        mCount = Counter(magazine)

        for val in rCount:
            if not (val in mCount and mCount[val] >= rCount[val]):
                return False

        return True