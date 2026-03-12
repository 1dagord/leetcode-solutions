/*
    [EASY]
    26. Remove Duplicates from Sorted Array

    Concepts:
    - array
    - two pointers

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.25 MB   [Beats 87.94%]
*/

impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        nums.dedup();
        return nums.len() as i32;
    }
}