"""
    [EASY]
    125. Valid Palindrome

    Concepts:
    - string
    - two pointers

    Stats:
        Runtime | 4 ms      [Beats 90.75%]
        Memory  | 18.40 MB  [Beats 41.66%]
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(list(filter(str.isalnum, s))).lower()
        n = len(s)

        for i in range((n + 1) // 2):
            if s[i] != s[-(i+1)]:
                return False
        return True