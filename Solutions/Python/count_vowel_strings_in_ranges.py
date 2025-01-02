"""
    [MEDIUM]
    2559. Count Vowel Strings in Ranges

    Concepts:
    - prefix sum
    - string

    Stats:
        Runtime | 24 ms     [Beats 35.91%]
        Memory  | 51 MB     [Beats 10.54%]
"""

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(queries)
        m = len(words)

        res = [0]*n
        vowels = set(["a", "e", "i", "o", "u"])

        pref = [0]*m
        pref[0] = int(words[0][0] in vowels and words[0][-1] in vowels)

        for i in range(1, m):
            pref[i] += pref[i-1] + int(
                words[i][0] in vowels and
                words[i][-1] in vowels
            )

        pref = [0] + pref

        for i, query in enumerate(queries):
            l, r = query
            res[i] = pref[r + 1] - pref[l]

        return res