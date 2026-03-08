/*
    [EASY]
    67. Add Binary

    Concepts:
    - bit manipulation
    - string

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.11 MB   [Beats 64.07%]
*/

use std::cmp;

impl Solution {
    pub fn add_binary(a: String, b: String) -> String {
        let mut res = Vec::new();
        let (mut x, mut y, mut value, mut carry) = (
            false, false, false, false
        );
        let max_len = cmp::max(a.len(), b.len());

        // pad out to same length
        let [a, b]: [Vec<char>; 2] = [a, b]
            .iter()
            .map(
                |s|
                format!("{s:0>width$}", width=max_len)
                    .chars()
                    .collect()
            )
            .collect::<Vec<Vec<char>>>()
            .try_into()
            .unwrap();

        // ripple carry adder
        for bit in (0..max_len).rev() {
            x = a[bit] == '1';
            y = b[bit] == '1';

            value = (x ^ y) ^ carry;
            carry = (carry && (x ^ y)) || (x && y);

            res.push(if value { '1' } else { '0' });
        }

        if carry { res.push('1'); }
        res.reverse();
        return res.iter().collect();
    }
}