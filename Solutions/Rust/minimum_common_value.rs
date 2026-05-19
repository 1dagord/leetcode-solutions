/*
    [EASY]
    2540. Minimum Common Value

    Concepts:
    - array
    - hash table

    Stats:
        Runtime | 1 ms      [Beats 28.57%]
        Memory  | 4.33 MB   [Beats 14.29%]
*/
use std::collections::BTreeSet;

impl Solution {
    pub fn get_common(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let one: BTreeSet<i32> = nums1.into_iter().collect();
        let two: BTreeSet<i32> = nums2.into_iter().collect();
        return match one.intersection(&two).next() {
            Some(&val) => val,
            None => -1
        };
    }
}