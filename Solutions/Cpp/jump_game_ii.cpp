/*
    [MEDIUM]
    45. Jump Game II

    Concepts:
    - array
    - dynamic programming

    Stats:
        Runtime | 651 ms    [Beats 5.01%]
        Memory  | 23.73 MB  [Beats 6.36%]
*/

class Solution {
public:
    int jump(vector<int>& nums) {
        int n = nums.size();
        vector<int> dp(n, std::numeric_limits<u_short>::max());

        std::function<int(u_short)> solve;

        solve = [&](u_short idx) {
            if (idx >= n-1)
                return 0;

            if (dp[idx] != std::numeric_limits<u_short>::max())
                return dp[idx];
            
            for (u_short j = nums[idx]; j > 0; j--) {
                dp[idx] = min(
                    dp[idx],
                    1 + solve(idx + j)
                );
            }

            return dp[idx];
        };

        return solve(0);
    }
};