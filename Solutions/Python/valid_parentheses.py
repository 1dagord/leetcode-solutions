"""
    [EASY]
    20. Valid Parentheses

    Concepts:
    - stack
    - string

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 16.71 MB  [Beats 100%]
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        brackets = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }

        for c in s:
            # if c is an opening bracket...
            if c in brackets:
                stack.append(c)
            else:
                if not stack:
                    return False
                    
                brack = stack.pop()
                if c != brackets[brack]:
                    return False

        return not bool(stack)