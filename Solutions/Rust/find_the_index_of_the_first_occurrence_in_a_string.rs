/*
    EASY]
    28. Find the Index of the First Occurrence in a String

    Concepts:
    - string
    - string matching

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.10 MB   [Beats 99.35%]
*/
impl Solution {
    pub fn str_str(haystack: String, needle: String) -> i32 {
        return match haystack.find(needle.as_str()) {
            Some(res) => res as i32,
            None => -1
        };
    }
}