"""
    [MEDIUM]
    1358. Number of Substrings Containing All Three Characters

    Concepts:
    - sliding window
    - string

    Stats:
        Runtime | 129 ms    [Beats 31.20%]
        Memory  | 17.78 MB  [Beats 90.82%]
"""

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        start, end = 0, 0
        n = len(s)

        abc = [0, 0, 0]

        index = lambda c: ord(c) - ord("a")

        while end < n:
            abc[index(s[end])] += 1

            # if current substring is valid...
            while start < end and all(abc):
                # ... all subsequent substrings also valid
                count += n - end
                abc[index(s[start])] -= 1

                start += 1
            
            end += 1

        return count