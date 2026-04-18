/*
    [EASY]
    3783. Mirror Distance of an Integer

    Concepts:
    - math

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.16 MB   [Beats 51.52%]
*/
impl Solution {
    pub fn mirror_distance(n: i32) -> i32 {
        return (
            n - (
                n
                .to_string()
                .chars()
                .rev()
                .collect::<String>()
                .parse::<i32>()
                .unwrap()
            )
        ).abs();
    }
}