/*
    [EASY]
    205. Isomorphic Strings

    Concepts:
    - string
    - hash table

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.42 MB   [Beats 25.00%]
*/
use std::collections::HashMap;

impl Solution {
    pub fn is_isomorphic(a: String, b: String) -> bool {
        let mut a_to_b: HashMap<char, char> = HashMap::new();
        let mut b_to_a: HashMap<char, char> = HashMap::new();
        let [mut x, mut y]: [char; 2];
        let [a_chars, b_chars]: [Vec<char>; 2] = [
            a.chars().collect(),
            b.chars().collect()
        ];

        for i in 0..a.len() {
            [x, y] = [a_chars[i], b_chars[i]];
            match a_to_b.get(&x) {
                Some(&v) => {
                    if v != y { return false; }
                },
                None => {
                    a_to_b.insert(x, y);
                }
            }

            match b_to_a.get(&y) {
                Some(&v) => {
                    if v != x { return false; }
                },
                None => {
                    b_to_a.insert(y, x);
                }
            }
        }

        return true;
    }
}