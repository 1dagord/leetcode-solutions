"""
    [MEDIUM]
    1415. The k-th Lexicographical String of All Happy Strings of Length n

    Concepts:
    - string
    - backtracking

    Stats:
        Runtime | 5 ms      [Beats 73.52%]
        Memory  | 18.33 MB  [Beats 32.60%]
"""

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        strings = []

        def solve(idx: int, string: list[str]) -> bool:
            nonlocal strings

            if idx == n:
                strings.append("".join(string))
                return len(strings) == k

            for letter in "abc":
                if string:
                    if letter != string[-1]:
                        if solve(idx + 1, string + [letter]):
                            return True
                else:
                    if solve(idx + 1, string + [letter]):
                        return True

            return False

        return strings[-1] if solve(0, []) else ""