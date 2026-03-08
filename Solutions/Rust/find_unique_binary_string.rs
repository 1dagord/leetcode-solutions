/*
    [MEDIUM]
    1980. Find Unique Binary String

    Concepts:
    - backtracking
    - hash table

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 17.90 MB  [Beats 52.45%]
*/

use std::collections::HashSet;

impl Solution {
    pub fn find_different_binary_string(nums: Vec<String>) -> String {
        let max_int: u64 = "1"
            .repeat(nums.len())
            .parse::<u64>()
            .unwrap();
        let nums: HashSet<u64> = HashSet::from_iter(
            nums
                .iter()
                .map(
                    |num| u64::from_str_radix(num, 2).unwrap()
                )
        );
        for num in 0..=max_int + 1 {
            if !nums.contains(&num) {
                return String::from(
                    format!(
                        "{num:0>width$b}"
                        , width=nums.len()
                    )
                );
            }
        }
        return "".to_string();
    }
}