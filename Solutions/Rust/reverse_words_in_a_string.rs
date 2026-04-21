/*
    [MEDIUM]
    151. Reverse Words in a String

    Concepts:
    - string

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.12 MB   [Beats 87.20%]
*/
impl Solution {
    pub fn reverse_words(s: String) -> String {
        return s
            .split_whitespace()
            .rev()
            .collect::<Vec<&str>>()
            .join(" ");
    }
}