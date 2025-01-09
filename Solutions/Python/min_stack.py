"""
    [MEDIUM]
    155. Min Stack

    Concepts:
    - stack
    - design

    Stats:
        Runtime | 11 ms     [Beats 25.74%]
        Memory  | 21.80 MB  [Beats 6.45%]
"""

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            self.stack.append(
                (
                    val,
                    self.stack[-1][1]
                    if self.stack[-1][1] < val
                    else val
                )
            )

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]