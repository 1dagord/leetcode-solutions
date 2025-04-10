/*
    [MEDIUM]
    137. Single Number II

    Concepts:
    - bit manupulation

    Stats:
        Runtime | 2 ms      [Beats 37.81%]
        Memory  | 13.39 MB  [Beats 65.66%]
*/

class Solution {
public:
    std::array<int, 32> XOR(std::array<int, 32> num1, int num2) {
        std::array<int, 32> res = {};

        for (int i = 0; i < 32; i++)
            res[i] = (num1[i] + ((num2 >> (31 - i)) & 1)) % 3;

        return res;
    }
    
    int singleNumber(vector<int>& nums) {
        std::array<int, 32> ans = {};

        for (int num : nums)
            ans = XOR(ans, num);

        long res = 0;
        bool is_negative = (ans.back() != 0);

        for (int i = 0; i < 32; i++)
            if ((!is_negative && ans[i] != 0) || (is_negative && ans[i] == 0))
                res |= (1 << (31 - i));

        if (is_negative)
            res = (-1 * res) - 1;

        return (int)res;
    }
};