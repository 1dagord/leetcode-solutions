/*
    [MEDIUM]
    55. Jump Game

    Concepts:
    - array
    - greedy

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.24 MB   [Beats 60.91%]
*/

impl Solution {
    pub fn can_jump(nums: Vec<i32>) -> bool {
        let mut goalpost = (nums.len() - 1) as i32;
        let mut i = goalpost;

        while i >= 0 {
            if goalpost - i <= nums[i as usize] {
                goalpost = i;
            }
            i -= 1;
        }

        return if goalpost == 0 { true } else { false };
    }
}