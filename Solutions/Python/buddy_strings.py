"""
    [EASY]
    859. Buddy Strings

    Concepts:
    - string
    - hash table

    Stats:
        Runtime | 3 ms      [Beats 48.18%]
        Memory  | 17.17 MB  [Beats 16.62%]
"""

from collections import Counter

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # disqualify if length difference > 1
        if len(s) != len(goal):
            return False
        
        n = len(s)
        a = [c for c in s]
        b = [c for c in goal]
        diff = {} # a[i] -> b[i]
        
        for i in range(n):
            if a[i] != b[i]:

                # to avoid collisions, hash index along with value
                if b[i] not in diff:
                    diff[(b[i], i)] = a[i]
                else:
                    if diff[(b[i], i)] != a[i]:
                        return False

        if len(diff) > 2:
            return False

        # check if keys and values map to each other
        if {k[0] : v for k, v in diff.items()} != {v : k[0] for k, v in diff.items()}:
            return False

        # if word is same already and every letter is
        # distinct, return False  
        return (a != b or len(Counter(s)) != len(s))