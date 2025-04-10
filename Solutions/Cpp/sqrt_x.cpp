/*
    [EASY]
    69. Sqrt(x)

    Concepts:
    - math
    - binary search

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 8.58 MB   [Beats 50.99%]
*/

class Solution {
public:
    int mySqrt(int x) {
        int l, m, r;
        l = 1, r = x;

        while (l <= r) {
            m = l + (r - l) / 2;

            if (std::pow(m, 2) < x)
                l = m + 1;
            else if (std::pow(m, 2) > x)
                r = m - 1;
            else
                return m;
        }

        return r;
    }
};