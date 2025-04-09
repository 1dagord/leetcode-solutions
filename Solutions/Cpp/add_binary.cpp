/*
    [EASY]
    67. Add Binary

    Concepts:
    - bit manipulation
    - string

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 9.02 MB   [Beats 44.94%]
*/

class Solution {
public:
    string addBinary(string a, string b) {
        std::string res = "";
        bool a_one, b_one, sum;
        bool carry = false;

        if (a.size() < b.size())
            std::swap(a, b);

        int diff = a.size() - b.size();

        for (int i = a.size() - 1; i > -1; i--) {
            a_one = a[i] == '1';
            b_one = (i >= diff) ? (b[i - diff] == '1') : (false);

            sum = (a_one ^ b_one) ^ (carry);
            carry = ((a_one ^ b_one) && carry) || (a_one && b_one);

            res += sum ? '1' : '0';
        }

        if (carry)
            res += '1';

        std::reverse(res.begin(), res.end());
        return res;
    }
};