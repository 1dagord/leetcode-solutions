"""
    [MEDIUM]
    5. Longest Palindromic Substring

    Concepts:
    - string
    - two pointers

    Stats:
        Runtime | 383 ms    [Beats 43.85%]
        Memory  | 17.67 MB  [Beats 96.22%]
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longest = ""

        def expand(left: int, right: int) -> str:
            palindrome = ""

            while left >= 0 and right < n and s[left] == s[right]:
                palindrome = s[left:right+1]
                left -= 1
                right += 1

            return palindrome

        for i in range(n):
            odd = expand(i, i)
            even = expand(i, i + 1)

            if len(odd) > len(longest):
                longest = odd
            if len(even) > len(longest):
                longest = even

        return longest