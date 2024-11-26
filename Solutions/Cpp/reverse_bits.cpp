/*
    [EASY]
    190. Reverse Bits

    Concepts:
    - bit manipulation

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 7.60 MB   [Beats 5.99%]
*/

class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t num = 0;
        for (int i = 0; i < 32; i++)
            num |= (((n & 1 << (31-i)) >> (31-i)) << i);
        return num;
    }
};