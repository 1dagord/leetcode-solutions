/*
    [MEDIUM]
    172. Factorial Trailing Zeroes

    Concepts:
    - math

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 8.32 MB   [Beats 3.62%]
*/

class Solution {
public:
    int trailingZeroes(int n) {
        /*
            Legendre's Formula

            Based on an infinite sum, but we can set the upper
            bound to the one given in the problem

            https://en.wikipedia.org/wiki/Legendre%27s_formula
        */
        int count = 0;

        for (int i = 1; std::pow(5, i) < std::pow(10, 4); i++)
            count += (n / std::pow(5, i));

        return count;
    }
};