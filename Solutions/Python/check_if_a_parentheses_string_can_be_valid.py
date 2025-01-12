"""
    [MEDIUM]
    2116. Check if a Parentheses String Can Be Valid

    Concepts:
    - string
    - greedy

    Stats:
        Runtime | 103 ms    [Beats 58.79%]
        Memory  | 18.58 MB  [Beats 57.06%]
"""

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        """
            Iterate forwards and backwards, first checking
            for unlocked indices and open parentheses

            If either iteration is unbalanced, return False
            Else, True
        """
        n = len(s)
        count = 0

        if n % 2 != 0:
            return False

        # left to right
        for i in range(n):
            count += 1 if locked[i] == "0" or s[i] == "(" else -1
        
            if count < 0:
                return False

        count = 0

        # right to left
        for i in reversed(range(n)):
            count += 1 if locked[i] == "0" or s[i] == ")" else -1

            if count < 0:
                return False

        return True