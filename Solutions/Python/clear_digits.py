"""
    [EASY]
    3174. Clear Digits

    Concepts:
    - string
    - stack

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 17.91 MB  [Beats 7.88%]
"""

class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []

        for c in s:
            if c.isalpha():
                stack.append(c)
            elif stack:
                stack.pop()

        return "".join(stack)
            