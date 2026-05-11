/*
    [HARD]
    30. Substring with Concatenation of All Words

    Concepts:
    - string
    - hash table
    - depth-first search

    Stats:
        Runtime | 232 ms    [Beats 12.73%]
        Memory  | 2.51 MB   [Beats 34.55%]
*/
use std::collections::{HashSet, HashMap};
use std::cmp::min;

impl Solution {
    pub fn find_substring(s: String, mut words: Vec<String>) -> Vec<i32> {
        if HashSet::<String>::from_iter(words.iter().cloned()).len() == 1 {
            words = vec![words.join("")];
        }

        let word_length: usize = words[0].len();
        let all_words_length: usize = word_length * words.len();
        let s_length: usize = s.len();

        let mut indices: Vec<i32> = Vec::new();
        let mut remaining: HashMap<String, usize> = HashMap::new();
        words
            .iter()
            .for_each(|word| {
                remaining
                    .entry(word.to_string())
                    .and_modify(|v| *v += 1)
                    .or_insert(1);
            });

        fn dfs(
            idx: usize,
            all_words_length: usize,
            word_length: usize,
            mut s: &str,
            mut indices: &mut Vec<i32>,
            mut remaining: &mut HashMap<String, usize> 
        ) {
            if remaining.is_empty() {
                indices.push(idx as i32 - all_words_length as i32);
                return;
            }
            if idx + word_length > s.len() { return; }

            let word: &str = &s[idx..idx+word_length];

            if remaining.contains_key(word) {
                remaining.entry(word.to_string()).and_modify(|v| *v -= 1);
                if *remaining.get(word).unwrap() == 0 {
                    remaining.remove(word);
                }

                dfs(
                    idx + word_length,
                    all_words_length,
                    word_length,
                    s,
                    &mut indices,
                    &mut remaining
                );

                remaining
                    .entry(word.to_string())
                    .and_modify(|v| *v += 1)
                    .or_insert(1);
            }
        };

        for i in 0..s_length {
            let substr = &s[i..min(i+word_length, s.len())];
            if remaining.contains_key(substr) {
                dfs(
                    i,
                    all_words_length,
                    word_length,
                    s.as_str(),
                    &mut indices,
                    &mut remaining
                );
            }
        }

        return indices;
    }
}