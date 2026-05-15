/*
    [MEDIUM]
    49. Group Anagrams

    Concepts:
    - hash table
    - string

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 4.26 MB   [Beats 96.69%]
*/
use std::collections::HashMap;

impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut res: HashMap<String, Vec<String>> = HashMap::new();
        let mut s_chars: Vec<char>;

        for s in strs {
            s_chars = s.chars().collect();
            s_chars.sort();
            res
                .entry(s_chars.iter().collect::<String>())
                .and_modify(|v| (*v).push(s.clone()))
                .or_insert(Vec::from([s]));
        }

        return res.into_values().collect();
    }
}