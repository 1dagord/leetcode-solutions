"""
    [MEDIUM]
    1930. Unique Length-3 Palindromic Subsequences

    Concepts:
    - hash table
    - string

    Stats:
        Runtime | 113 ms    [Beats 81.31%]
        Memory  | 18.39 MB  [Beats 42.69%]
"""

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        """
            Return number of unique 3-char palindromes that
            are subsequence of s

            For each letter, find first and last occurance, then
            add number of unique chars between to count
        """
        n = len(s)
        visited = set()
        count = 0

        def getVal(key: str):
            return n - s[::-1].find(key) - 1

        last_occurances = {
            (key := chr(ord("a") + i)) :
            getVal(key)
            for i in range(26)
        }

        for start, c in enumerate(s):
            if c not in visited:
                if (end := last_occurances[c]) != -1:
                    count += len(set(s[start+1:end]))
                visited.add(c)

        return count