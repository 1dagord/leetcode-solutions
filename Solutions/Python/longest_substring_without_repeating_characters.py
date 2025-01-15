"""
    [MEDIUM]
    3. Longest Substring Without Repeating Characters

    Concepts:
    - sliding window
    - hash table

    Stats:
        Runtime | 15 ms     [Beats 81.90%]
        Memory  | 18.04 MB  [Beats 6.50%]
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        start = 0
        seen = set()

        for end in range(len(s)):
            while s[end] in seen:
                seen.remove(s[start])
                start += 1

            seen.add(s[end])

            longest = max(longest, end - start + 1)

        return longest