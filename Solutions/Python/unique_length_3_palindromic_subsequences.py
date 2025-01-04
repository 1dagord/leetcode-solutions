"""
    [MEDIUM]
    1930. Unique Length-3 Palindromic Subsequences

    Concepts:
    - hash table
    - string

    Stats:
        Runtime | 135 ms    [Beats 81.32%]
        Memory  | 18.36 MB  [Beats 22.86%]
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
            try:
                return n - s[::-1].index(key) - 1
            except ValueError:
                return -1

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