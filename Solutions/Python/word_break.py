"""
    [MEDIUM]
    139. Word Break

    Concepts:
    - string
    - hash table
    - dynamic programming

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 16.66 MB  [Beats 100%]
"""

class Solution:
    def wordBreak(self, s: str, word_list: List[str]) -> bool:
        n = len(s)
        # store true at dp[i] if s[i:] contains words in dictionary
        dp = [False]*(n+1)
        # if at end of string, true
        dp[n] = True

        for i in range(n-1, -1, -1):
            for word in word_list:
                word_len = len(word)
                # if `word` fits in substring starting at `i` and
                # can find word starting at index `i`...
                if (i + word_len) <= n and s[i:i+word_len] == word:
                    # set dp[i] equal to value of dp `word_len` letters ahead
                    dp[i] = dp[i + word_len]
                if dp[i]:
                    break

        return dp[0]