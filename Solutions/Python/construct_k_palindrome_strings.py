"""
    [MEDIUM]
    1400. Construct K Palindrome Strings

    Concepts:
    - hash table
    - string

    Stats:
        Runtime | 27 ms     [Beats 93.55%]
        Memory  | 18.19 MB  [Beats 19.36%]
"""

from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        """
            String is palindrome every character appears
            even number of times (except maybe one)
        """
        if len(s) < k:
            return False
            
        return (
            len(
                [(key, val) for key, val in Counter(s).items() if val % 2 != 0]
            ) <= k
        )
