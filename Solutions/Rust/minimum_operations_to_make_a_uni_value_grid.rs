/*
    [MEDIUM]
    2033. Minimum Operations to Make a Uni-Value Grid

    Concepts:
    - array
    - math

    Stats:
        Runtime | 14 ms     [Beats 50.00%]
        Memory  | 8.55 MB   [Beats 25.00%]
*/
impl Solution {
    pub fn min_operations(grid: Vec<Vec<i32>>, x: i32) -> i32 {
        let mut values = grid
            .into_iter()
            .flatten()
            .collect::<Vec<i32>>();
        values.sort();
        let n = values.len();

        if n == 1 {
            return 0;
        }

        if !values.iter().all(|&val| (val % x) == (values[0] % x)) {
            return -1;
        }

        return values
            .iter()
            .map(|&val| (values[n / 2] - val).abs() / x)
            .fold(0, |a, b| a + b);
    }
}