/*
    [EASY]
    242. Valid Anagram

    Concepts:
    - string
    - hash table

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.37 MB   [Beats 37.29%]
*/
use std::collections::HashMap;

impl Solution {
    pub fn is_anagram(a: String, b: String) -> bool {
        if a.len() != b.len() { return false; }
        let mut a_cntr = HashMap::new();
        let mut b_cntr = HashMap::new();

        for (s, cntr) in [(a, &mut a_cntr), (b, &mut b_cntr)] {
            s
                .chars()
                .for_each(|c| {
                    cntr
                        .entry(c)
                        .and_modify(|v| *v += 1)
                        .or_insert(1);
                });
        }

        return a_cntr == b_cntr;
    }
}