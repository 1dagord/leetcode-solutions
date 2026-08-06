/*
    [EASY]
    3345. Smallest Divisible Digit Product I

    Concepts:
    - math
    - enumeration

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.06 MB   [Beats 93.33%]
*/
impl Solution {
    pub fn smallest_number(n: i32, t: i32) -> i32 {
        fn digit_product(num: i32) -> i32 {
            return num
                .to_string()
                .chars()
                .map(|v| v as i32 - '0' as i32)
                .fold(1, |a, b| a * b);
        }

        for num in n..=100 {
            if digit_product(num) % t == 0 {
                return num;
            }
        }

        return 0;
    }
}
