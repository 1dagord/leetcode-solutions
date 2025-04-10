/*
    [EASY]
    136. Single Number

    Concepts:
    - bit manipulation

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 20.59 MB  [Beats 83.47%]
*/

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        return std::reduce(nums.begin(), nums.end(), 0, std::bit_xor<int>());
    }
};