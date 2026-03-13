/*
    [MEDIUM]
    189. Rotate Array

    Concepts:
    - array
    - math

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 3.69 MB   [Beats 54.84%]
*/

impl Solution {
    pub fn rotate(nums: &mut Vec<i32>, k: i32) {
        let n = nums.len();
        nums.rotate_right((k as usize) % n);
    }
}