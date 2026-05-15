/*
    [EASY]
    1. Two Sum

    Concepts:
    - hash table

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 3.10 MB   [Beats 5.47%]
*/
use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut seen: HashMap<i32, Vec<i32>> = HashMap::new();

        for (i, &num) in nums.iter().enumerate() {
            seen
                .entry(num)
                .and_modify(|v| (*v).push(i as i32))
                .or_insert(Vec::from([i as i32]));

            match (seen.get(&(target - num)), seen.get(&num)) {
                (Some(v), Some(t)) => {
                    if v[0] != i as i32 {
                        if num == target - num { return t.clone(); }
                        else { return Vec::from([t[0], v[0]]); }
                    }
                },
                _ => {}
            }
        }

        return Vec::new();
    }
}