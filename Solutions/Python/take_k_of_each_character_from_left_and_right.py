"""
    [MEDIUM]
    2516. Take K of Each Character From Left and Right

    Concepts:
    - sliding window
    - hash table

    Stats:
        Runtime | 412 ms    [Beats 20%]
        Memory  | 17.17 MB  [Beats 79.81%]
"""

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        """
            Sliding Window
        """
        n = len(s)
        chars = {"a" : 0, "b" : 0, "c" : 0}

        for c in s:
            chars[c] += 1

        # check char frequency
        if not all([val >= k for val in chars.values()]):
            return -1

        res = n
        l = 0

        # shift in right pointer
        for r in range(n):
            chars[s[r]] -= 1

            # while condition not met, increment left
            while not all([val >= k for val in chars.values()]):
                chars[s[l]] += 1
                l += 1
            res = min(res, n - (r - l + 1))

        return res