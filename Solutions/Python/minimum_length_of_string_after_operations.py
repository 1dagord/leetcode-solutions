"""
    [MEDIUM]
    3223. Minimum Length of String After Operations

    Concepts:
    - string
    - hash table

    Stats:
        Runtime | 138 ms    [Beats 75.65%]
        Memory  | 18.87 MB  [Beats 52.77%]
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