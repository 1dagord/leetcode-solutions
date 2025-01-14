"""
    [MEDIUM]
    3223. Minimum Length of String After Operations

    Concepts:
    - string
    - hash table

    Stats:
        Runtime | 384 ms    [Beats 12.66%]
        Memory  | 19.02 MB  [Beats 7.08%]
"""

from collections import Counter

class Solution:
    def minimumLength(self, s: str) -> int:
        """
            If at least 3 occurrences of char,
            delete two until less than 3 remain
        """
        counter = Counter(s)

        for k in counter:
            if counter[k] >= 3:
                counter[k] = 1 + int(counter[k] % 2 == 0)

        return sum([v for v in counter.values()])