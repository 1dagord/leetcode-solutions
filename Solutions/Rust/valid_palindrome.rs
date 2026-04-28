/*
    [EASY]
    125. Valid Palindrome

    Concepts:
    - string
    - two pointers

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.39 MB   [Beats 71.18%]
*/
impl Solution {
    pub fn is_palindrome(_s: String) -> bool {
        let s = _s
            .to_lowercase()
            .chars()
            .filter(|&c| c.is_alphanumeric())
            .collect::<String>();
        return s == s.chars().rev().collect::<String>();
    }
}