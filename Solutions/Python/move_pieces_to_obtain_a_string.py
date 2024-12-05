"""
    [MEDIUM]
    2337. Move Pieces to Obtain a String

    Concepts:
    - string

    Stats:
        Runtime | 195 ms    [Beats 22.58%]
        Memory  | 38.47 MB  [Beats 6.59%]
"""

class Solution:
    def canChange(self, start: str, target: str) -> bool:
        """
            1) store indices of all Ls and Rs
            2) iterate over each char in target, checking
                if next matching char in start is valid
            3) if any discrepancy found, return False
        """
        s_chars = [(i, x) for i, x in enumerate(start) if x in "LR"]
        t_chars = [(i, x) for i, x in enumerate(target) if x in "LR"]

        if len(s_chars) != len(t_chars):
            return False

        for i in range(len(s_chars)):
            si, sx = s_chars[i]
            ti, tx = t_chars[i]

            if sx != tx:
                return False

            if sx == "L":
                if ti > si:
                    return False
            elif sx == "R":
                if ti < si:
                    return False

        return True