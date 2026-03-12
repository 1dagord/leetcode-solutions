/*
    [EASY]
    169. Majority Element

    Concepts:
    - array
    - counting

    Stats:
        Runtime | 2 ms      [Beats 24.40%]
        Memory  | 2.40 MB   [Beats 40.91%]
*/

use std::collections::HashMap;

impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> i32 {
        let mut counter = HashMap::<i32, i32>::new();

        for num in nums.iter() {
            *(counter.entry(*num).or_insert(0)) += 1;
            if counter[num] > (nums.len() as i32) / 2 {
                return *num;
            }
        }

        return 0;
    }
}