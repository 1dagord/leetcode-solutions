/*
    [MEDIUM]
    788. Rotated Digits

    Concepts:
    - math
    - dynamic programming

    Stats:
        Runtime | 6 ms      [Beats 9.52%]
        Memory  | 2.20 MB   [Beats 52.38%]
*/
use std::collections::HashMap;

impl Solution {
    pub fn rotated_digits(n: i32) -> i32 {
        let digit_map = HashMap::<char, char>::from([
            ('0', '0'),
            ('1', '1'),
            ('8', '8'),
            ('2', '5'),
            ('5', '2'), 
            ('6', '9'),
            ('9', '6')
        ]);

        let check = |num: i32| {
            let num_str = num.to_string();
            let mut res = String::new();

            for digit in num_str.chars() {
                match digit_map.get(&digit) {
                    Some(&p) => res.push(p),
                    None => return false
                }
            }

            return num != res.to_string().parse::<i32>().unwrap();
        };

        return (0..=n)
            .map(|i| if check(i) { 1 } else { 0 })
            .fold(0, |a, b| a + b);
    }
}