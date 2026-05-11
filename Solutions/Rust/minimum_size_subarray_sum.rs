/*
    [MEDIUM]
    209. Minimum Size Subarray Sum

    Concepts:
    - array
    - sliding window

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 3.02 MB   [Beats 19.23%]
*/
impl Solution {
    pub fn min_sub_array_len(target: i32, nums: Vec<i32>) -> i32 {
        let n = nums.len() as i32;
        let mut min_len: i32 = n + 1;
        let [mut left, mut curr_sum] = [0, 0];

        for right in 0..n {
            curr_sum += nums[right as usize];

            while curr_sum >= target {
                if right - left + 1 < min_len {
                    min_len = right - left + 1;
                }

                curr_sum -= nums[left as usize];
                left += 1;
            }
        }

        return if (min_len < n + 1) { min_len } else { 0 };
    }
}