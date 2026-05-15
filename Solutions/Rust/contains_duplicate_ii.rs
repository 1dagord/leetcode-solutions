/*
    [EASY]
    219. Contains Duplicate II

    Concepts:
    - array
    - hash table

    Stats:
        Runtime | 17 ms     [Beats 27.40%]
        Memory  | 4.80 MB   [Beats 47.26%]
*/
use std::collections::HashMap;

impl Solution {
    pub fn contains_nearby_duplicate(nums: Vec<i32>, k: i32) -> bool {
        let mut idx: HashMap<i32, i32> = HashMap::new();

        for i in 0..nums.len() {
            match idx.get(&nums[i]) {
                Some(&v) => {
                    if (i as i32 - v).abs() <= k {
                        return true;
                    }
                },
                None => {}
            }
            idx.insert(nums[i], i as i32);
        }

        return false;
    }
}