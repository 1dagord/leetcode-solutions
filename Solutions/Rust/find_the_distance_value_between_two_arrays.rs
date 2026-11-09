/*
    [EASY]
    1385. Find the Distance Value Between Two Arrays

    Concepts:
    - array
    - two pointers

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.16 MB   [Beats 56.22%]
*/
impl Solution {
    pub fn find_the_distance_value(arr1: Vec<i32>, arr2: Vec<i32>, d: i32) -> i32 {
        return arr1
            .iter()
            .map(|&a| {
                let is_less_than_or_equal = arr2.iter().any(|&b| (a - b).abs() <= d);
                return if is_less_than_or_equal { 0 } else { 1 };
            })
            .sum::<i32>();
    }
}
