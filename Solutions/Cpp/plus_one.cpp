/*
    [EASY]
    66. Plus One

    Concepts:
    - math

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 11.60 MB  [Beats 34.92%]
*/

class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int carry = 1, sum = 0;

        for (int i = digits.size() - 1; i > -1; i--) {
            sum = digits[i] + carry;

            carry = (sum > 9) ? 1 : 0;
            digits[i] = sum % 10;
        }

        if (carry)
            digits.insert(digits.begin(), 1);

        return digits;
    }
};