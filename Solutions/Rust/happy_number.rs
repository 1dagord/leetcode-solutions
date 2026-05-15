/*
    [EASY]
    202. Happy Number

    Concepts:
    - math
    - hash table

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.08 MB   [Beats 96.97%]
*/
use std::collections::HashSet;

impl Solution {
    pub fn is_happy(mut n: i32) -> bool {
        let mut visited: HashSet<i32> = HashSet::new();
        let mut number: String;
        let mut nums: Vec<i32>;

        while n != 1 {
            number = n.to_string();
            nums = number
                .chars()
                .map(|d| (d as i32 - '0' as i32).pow(2))
                .collect();
            n = nums.iter().sum();

            if visited.contains(&n) { return false; }
            visited.insert(n);
        }

        return true;
    }
}