/*
    [EASY]
    70. Climbing Stairs

    Concepts:
    - math
    - dynamic programming

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 8.61 MB   [Beats 17.41%]
*/

class Solution {
public:
    int climbStairs(int n) {
        std::unordered_map<int, int> dp = {
            {1, 1},
            {2, 2}
        };

        std::function<int(int)> solve;
        solve = [&](int n){
            // return value if already found
            if (dp.contains(n))
                return dp[n];
            // use sum of previous 2 to get next
            dp[n] = solve(n-1) + solve(n-2);

            return dp[n];
        };

        return solve(n);
    }
};