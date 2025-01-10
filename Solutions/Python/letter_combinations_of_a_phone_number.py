"""
    [MEDIUM]
    17. Letter Combinations of a Phone Number

    Concepts:
    - backtracking
    - hash table
    - string

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 16.56 MB  [Beats 98.04%]
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_to_let = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        # traverse k-ary tree in recursion and
        # loop over first chars in a loop

        def recurse(digits, combo, combos):
            # if at leaf, add path
            if not digits:
                combos.append(combo)
                return combo
            
            # add child to path, then call function on child
            for c in num_to_let[digits[0]]:
                recurse(digits[1:], combo + c, combos)

            return combos

        combos = []
        if digits:
            recurse(digits, "", combos)

        return combos