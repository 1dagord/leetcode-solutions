"""
    [MEDIUM]
    2825. Make String a Subsequence Using Cyclic Increments

    Concepts:
    - string
    - two pointers

    Stats:
        Runtime | 117 ms    [Beats 13.20%]
        Memory  | 17.5 MB   [Beats 50.24%]
"""

class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:

        n1 = len(str1)
        n2 = len(str2)

        def isAdjacent(c1: str, c2: str) -> bool:
            # returns true if chars c1 and c2 are cyclically adjacent
            if (c1, c2) == ("z", "a"):
                return True
            return ord(c2.lower()) - ord(c1.lower()) == 1

        i1, i2 = 0, 0
        while i1 < n1 and i2 < n2:
            if str1[i1] == str2[i2] or isAdjacent(str1[i1], str2[i2]):
                i2 += 1
            i1 += 1

        # true if all of str2 has been found within str1
        return i2 == n2