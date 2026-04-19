/*
    [EASY]
    13. Roman to Integer

    Concepts:
    - string
    - hash table

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.09 MB   [Beats 94.35%]
*/
use std::collections::HashMap;

impl Solution {
    pub fn roman_to_int(s: String) -> i32 {
        let n = s.len();
        let [mut num, mut i]: [usize; 2] = [0, 0];
        let [mut cur, mut nxt]: [char; 2] = ['a', 'a'];
        let r_to_i: HashMap<char, usize> = HashMap::from([
            ('I', 1),
            ('V', 5),
            ('X', 10),
            ('L', 50),
            ('C', 100),
            ('D', 500),
            ('M', 1000)
        ]);

        while i < n {
            cur = s.chars().nth(i).unwrap();
            if let nxt = s.chars().nth(i+1)
                && nxt.is_some()
                && (r_to_i[&cur] < r_to_i[&nxt.unwrap()])
            {
                num += r_to_i[&nxt.unwrap()] - r_to_i[&cur];
                i += 1;
            } else {
                num += r_to_i[&cur];
            }
            i += 1;
        }

        return num as i32;
    }
}