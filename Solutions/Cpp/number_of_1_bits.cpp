/*
    [EASY]
    191. Number of 1 Bits

    Concepts:
    - bit manipulation

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 6.06 MB   [Beats 100%]
*/

class Solution {
public:
    int hammingWeight(uint32_t n) {
        int hWeight = 0;
        for (int bitShift = 0; bitShift < 8*sizeof(uint32_t); bitShift++){
            hWeight += ((n & (1 << bitShift)) >> bitShift);
        }
        return hWeight;
    }
};