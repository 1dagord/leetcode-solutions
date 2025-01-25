"""
    [MEDIUM]
    12. Integer to Roman

    Concepts:
    - string
    - hash table

    Stats:
        Runtime | 4 ms      [Beats 65.94%]
        Memory  | 17.77 MB  [Beats 47.65%]
"""

from collections import defaultdict

class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ""
        roman_nums = {
            1000 : "M",
            900 : "CM",
            500 : "D",
            400 : "CD",
            100 : "C",
            90 : "XC",
            50 : "L",
            40 : "XL",
            10 : "X",
            9 : "IX",
            5 : "V",
            4 : "IV",
            1 : "I"
        }

        roman_count = defaultdict(int)

        for key in roman_nums.keys():
            while num >= key:
                roman_count[key] += 1
                num -= key

        for key, val in roman_count.items():
            roman += roman_nums[key]*val
            
        return roman