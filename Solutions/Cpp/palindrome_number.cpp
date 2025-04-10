/*
    [EASY]
    9. Palindrome Number

    Concepts:
    - math

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 8.50 MB   [Beats 68.99%]
*/

class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0)
            return false;
        
        long comp = 0;
        int num = x;

        while (x) {
            comp = (comp * 10) + (x % 10);
            x /= 10;
        }

        return (int)comp == num;
    }
};