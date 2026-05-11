/*
    [MEDIUM]
    3. Longest Substring Without Repeating Characters

    Concepts:
    - sliding window
    - hash table

    Stats:
        Runtime | 1 ms      [Beats 60.29%]
        Memory  | 2.32 MB   [Beats 32.19%]
*/
use std::collections::HashSet;
use std::cmp::max;

impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let mut longest = 0;
        let mut start = 0;
        let mut seen = HashSet::new();
        let chars = s.chars().collect::<Vec<char>>();

        for end in 0..chars.len() {
            while seen.contains(&chars[end]) {
                seen.remove(&chars[start]);
                start += 1
            }

            seen.insert(chars[end]);
            longest = max(longest, end - start + 1);
        }

        return longest as i32;
    }
}