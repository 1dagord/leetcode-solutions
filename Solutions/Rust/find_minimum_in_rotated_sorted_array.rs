/*
    [MEDIUM]
    153. Find Minimum in Rotated Sorted Array

    Concepts:
    - array
    - binary search

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.12 MB   [Beats 71.08%]
*/
impl Solution {
    pub fn find_min(nums: Vec<i32>) -> i32 {
        let [mut l, mut m, mut r] = [0, 0, nums.len() - 1];

        while l <= r {
            m = l + (r - l) / 2;

            if nums[l] > nums[r] {
                if nums[m] >= nums[l] { l = m + 1; }
                else { r = m; }
            } else {
                return nums[l];
            }
        }

        return nums[r];
    }
}