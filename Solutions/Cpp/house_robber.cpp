/*
    [MEDIUM]
    198. House Robber

    Concepts:
    - dynamic programming

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 10.87 MB  [Beats 6.05%]
*/

class Solution {
public:
    int rob(vector<int>& nums) {
        // initialize to impossible value
        std::vector<int> dp((int)nums.size(), -1);
        dp[0] = nums[0];

        std::function<int(int)> burgle;
        burgle = [&](int i){
            // if at end of street, no money can be made
            if (i < 0)
                return 0;
            
            // if already robbed this house, take money
            // from it and all eligible houses after
            if (dp[i] != -1)
                return dp[i];

            // either rob current house and house two houses down
            // or rob next house down and every eligible house before that
            dp[i] = std::max(
                nums[i] + burgle(i-2),
                burgle(i-1)
            );

            // once end of block reached, save loot starting from `i`
            return dp[i];
        };

        return burgle(nums.size() - 1);
    }
};