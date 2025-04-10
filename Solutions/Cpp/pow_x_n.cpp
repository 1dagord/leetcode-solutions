/*
    [MEDIUM]
    50. Pow(x, n)

    Concepts:
    - math
    - recursion

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 8.48 MB   [Beats 92.41%]
*/

class Solution {
public:
    double myPow(double x, long n) {
        if (n == 0)
            return 1.0;
        else if (n < 0)
            return 1.0 / myPow(x, -n);
        else if (n & 1)
            return myPow(x * x, n / 2) * x;
        else
            return myPow(x * x, n / 2);
    }
};