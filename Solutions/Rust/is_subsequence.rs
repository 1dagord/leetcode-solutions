/*
    [EASY]
    392. Is Subsequence

    Concepts:
    - string
    - two pointers

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.18 MB   [Beats 67.10%]
*/
impl Solution {
    pub fn is_subsequence(_s: String, _t: String) -> bool {
        let [s, t]: [Vec<char>; 2] = [_s.chars().collect(), _t.chars().collect()];
        let [mut i, mut j] = [0, 0];
        while i < s.len() && j < t.len() {
            if s[i] == t[j] {
                i += 1;
            }
            j += 1;
        }
        return i == s.len();
    }
}