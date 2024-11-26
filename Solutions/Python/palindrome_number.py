"""
    [EASY]
    9. Palindrome Number

    Concepts:
    - math

    Stats:
        Runtime | 11 ms     [Beats 36.36%]
        Memory  | 17.24 MB  [Beats 10.61%]
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        comp = 0
        num = x

        while x:
            comp = (comp * 10) + (x % 10)
            x //= 10
            
        return comp == num