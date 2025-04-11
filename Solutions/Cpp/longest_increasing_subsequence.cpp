/*
    [MEDIUM]
    300. Longest Increasing Subsequence

    Concepts:
    - array
    - dynamic programming

    Stats:
        Runtime | 43 ms     [Beats 73.48%]
        Memory  | 14.44 MB  [Beats 45.62%]
*/

class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        std::vector<int> dp(nums.size(), 1);

        for (int i = 1; i < nums.size(); i++)
            for (int j = 0; j < i; j++)
                if (nums[i] > nums[j])
                    dp[i] = std::max(dp[i], dp[j] + 1);

        return *(std::max_element(dp.begin(), dp.end()));
    }
};