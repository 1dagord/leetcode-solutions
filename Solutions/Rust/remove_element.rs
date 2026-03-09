/*
    [EASY]
    27. Remove Element

    Concepts:
    - array

    Stats:
        Runtime | 0 ms      [Beast 100%]
        Memory  | 2.17 MB   [Beats 64.71%]
*/

impl Solution {
    pub fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
        nums.retain(|&num| num != val);
        return nums.len() as i32;
    }
}