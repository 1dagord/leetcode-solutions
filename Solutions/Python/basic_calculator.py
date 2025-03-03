"""
    [HARD]
    224. Basic Calculator

    Concepts:
    - stack
    - math
    - string

    Stats:
        Runtime | 19 ms     [Beats 94.77%]
        Memory  | 18.19 MB  [Beats 92.67%]
"""

class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")

        output = 0
        curr, sign = 0, 1
        stack = []

        for c in s:
            if c.isdigit():
                # account for multi-digit numbers
                curr = curr*10 + int(c)

            elif c in "+-":
                # store what we calculated so far
                output += (curr * sign)
                # reset current sum
                curr = 0
                # set sign
                sign = -1 if c == "-" else 1

            elif c == "(":
                # store current output and reset
                stack.append(output)
                output = 0
                # store current sign and reset
                stack.append(sign)
                sign = 1

            elif c == ")":
                # add current value
                output += (curr * sign)
                # multiply by last stored sign
                output *= stack.pop()
                # add to last stored sum
                output += stack.pop()
                # reset current sum
                curr = 0

        return output + (curr * sign)