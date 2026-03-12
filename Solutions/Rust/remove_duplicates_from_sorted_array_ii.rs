/*
    [MEDIUM]
    80. Remove Duplicates from Sorted Array II

    Concepts:
    - array
    - two pointers

    Stats:
        Runtime | 3 ms      [Beats 70.14%]
        Memory  | 2.14 MB   [Beats 96.83%]
*/

impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        if nums.len() <= 2 {
            return nums.len() as i32;
        }

        let mut k = 2;
        for i in 2..nums.len() {
            if nums[i] != nums[k-2] {
                nums[k] = nums[i];
                k += 1;
            }
        }

        return k as i32;
    }
}