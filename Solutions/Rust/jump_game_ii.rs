/*
    [MEDIUM]
    45. Jump Game II

    Concepts:
    - array
    - dynamic programming

    Stats:
        Runtime | 107 ms    [Beats 7.10%]
        Memory  | 2.72 MB   [Beats 5.16%]
*/
use std::cmp::min;

impl Solution {
    pub fn jump(nums: Vec<i32>) -> i32 {
        const INF: i32 = i32::MAX - 1;
        let mut dp = vec![INF; nums.len()];

        fn solve (idx: usize, dp: &mut Vec<i32>, nums: &Vec<i32>) -> i32 {
            if (idx >= nums.len() - 1) { return 0; }
            if (dp[idx] != INF) { return dp[idx]; }

            for j in (1..=nums[idx]).rev() {
                dp[idx] = min(
                    dp[idx]
                    , 1 + solve(idx + (j as usize), dp, nums)
                );
            }

            return dp[idx];
        };

        return solve(0, &mut dp, &nums);
    }
}