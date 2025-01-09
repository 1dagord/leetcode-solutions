"""
    [MEDIUM]
    3042. Count Prefix and Suffix Pairs I

    Concepts:
    - string
    - string matching

    Stats:
        Runtime | 7 ms      [Beats 89.31%]
        Memory  | 17.61 MB  [Beats 36.75%]
"""

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        count = 0
        
        def isPrefixAndSuffix(s1: str, s2: str) -> bool:
            n1 = len(s1)
            return (s2[:n1] == s1 and s2[-n1:] == s1)

        for j in range(n):
            for i in range(j):
                if isPrefixAndSuffix(words[i], words[j]):
                    count += 1

        return count