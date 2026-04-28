/*
    [MEDIUM]
    11. Container With Most Water

    Concepts:
    - array
    - two pointers

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.88 MB   [Beats 99.58%]
*/
use std::cmp::{min, max};

impl Solution {
    pub fn max_area(mut height: Vec<i32>) -> i32 {
        let mut max_water: usize = 0;
        let n: usize = height.len();
        let [mut left, mut right]: [usize; 2] = [0, n-1];

        while left < right {
            max_water = max(
                max_water,
                min(
                    height[left],
                    height[right]
                ) as usize * (right - left)
            );

            if height[left] > height[right] { right -= 1; }
            else { left += 1; }
        }

        return max_water as i32;
    }
}