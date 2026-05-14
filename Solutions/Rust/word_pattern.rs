/*
    [EASY]
    290. Word Pattern

    Concepts:
    - string
    - hash table

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.20 MB   [Beats 86.44%]
*/
use std::collections::HashMap;

impl Solution {
    pub fn word_pattern(pattern: String, s: String) -> bool {
        let words: Vec<&str> = s.split(" ").collect();
        let chars: Vec<char> = pattern.chars().collect();
        let mut s_to_p: HashMap<&str, char> = HashMap::new();
        let mut p_to_s: HashMap<char, &str> = HashMap::new();
        let (mut c, mut w): (char, &str);

        if pattern.len() != words.len() { return false; }

        for i in 0..words.len() {
            (c, w) = (chars[i], words[i]);
            if (
                (p_to_s.contains_key(&c) && *p_to_s.get(&c).unwrap() != w)
                || (s_to_p.contains_key(&w) && *s_to_p.get(&w).unwrap() != c)
            ) {
                return false;
            }
            p_to_s.insert(c, w);
            s_to_p.insert(w, c);
        }

        return true;
    }
}