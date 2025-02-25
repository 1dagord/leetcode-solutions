"""
    [MEDIUM]
    150. Evaluate Reverse Polish Notation

    Concepts:
    - stack
    - math

    Stats:
        Runtime | 3 ms      [Beats 64.95%]
        Memory  | 19.17 MB  [Beats 52.33%]
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {"+", "-", "*", "/"}

        for c in tokens:
            if c in ops:
                b, a = stack.pop(), stack.pop()

                if c == "+":
                    stack.append(a + b)
                elif c == "-":
                    stack.append(a - b)
                elif c == "*":
                    stack.append(a * b)
                else:
                    stack.append(
                        a // b
                        if (a > 0 and b > 0)
                        or (a < 0 and b < 0)
                        else ceil(a / b)
                    )
            else:
                stack.append(int(c))

        return stack[0]