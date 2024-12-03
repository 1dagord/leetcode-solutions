"""
    [MEDIUM]
    2109. Adding Spaces to a String

    Concepts:
    - string
    - two pointers

    Stats:
        Runtime | 131 ms    [Beats 31.78%]
        Memory  | 48.7 MB   [Beats 58.55%]
"""

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:

        n = len(s)
        k = len(spaces)
        res = [""]*(n + k)

        i = 0   # spaces pointer
        j = 0   # s pointer

        while j < n:
            # if has spaces to insert and reached space index...
            if i < k and j == spaces[i]:
                res[j + i] = " "
                i += 1

            # if no spaces to insert or not at space index...
            else:
                res[j + i] = s[j]
                j += 1

        return "".join(res)
