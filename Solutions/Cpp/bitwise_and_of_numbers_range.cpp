/*
    [MEDIUM]
    201. Bitwise AND of Numbers Range

    Concepts:
    - bit manipulation

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 11.35 MB  [Beats 13.33%]
*/

class Solution {
public:
    int rangeBitwiseAnd(int left, int right) {
        /*
            For every set number represented by a
            single set bit, if 1 - number is in range,
            that bit must be reset in the answer
        */
        while (right > left)
            right &= right - 1;
        return right;
    }
};