"""
    [MEDIUM]
    71. Simplify Path

    Concepts:
    - stack
    - string

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 16.58 MB  [Beats 100%]
"""

class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split("/")
        stack = []

        for dir in dirs:
            if dir:
                if dir == "..":
                    if stack:
                        stack.pop()
                elif dir == ".":
                    continue
                else:
                    stack.append(dir)

        return "/" + "/".join(stack)