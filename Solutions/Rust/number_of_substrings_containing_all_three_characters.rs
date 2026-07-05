/*
    [MEDIUM]
    1358. Number of Substrings Containing All Three Characters

    Concepts:
    - string
    - hash table

    Stats:
        Runtime | 1 ms      [Beats 83.43%]
        Memory  | 2.30 MB   [Beats 66.00%]
*/
use std::collections::HashMap;

impl Solution {
    pub fn number_of_substrings(st: String) -> i32 {
        let mut counter: [usize; 3] = [0; 3];
        let mut num_substrings: usize = 0;

        let s: Vec<char> = st.chars().collect();
        let n: usize = s.len();
        let mut i: usize = 0;
        for j in 0..n {
            counter[s[j] as usize - 'a' as usize] += 1;
            while counter[0] != 0 && counter[1] != 0 && counter[2] != 0 {
                num_substrings += n - j;
                counter[s[i] as usize - 'a' as usize] -= 1;
                i += 1;
            }
        }

        return num_substrings as i32;
    }
}
