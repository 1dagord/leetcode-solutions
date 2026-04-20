/*
    [EASY]
    58. Length of Last Word

    Concepts:
    - string

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.22 MB   [Beats 16.46%]
*/
impl Solution {
    pub fn length_of_last_word(s: String) -> i32 {
        return s.trim().split(" ").last().unwrap().len() as i32;
    }
}