/*
    [HARD]
    42. Trapping Rain Water

    Concepts:
    - array
    - prefix/suffix maximum

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.39 MB   [Beats 28.57%]
*/
use std::cmp::{max, min};

impl Solution {
    pub fn trap(height: Vec<i32>) -> i32 {
        let n: usize = height.len();
        let mut water: i32 = 0;

        // prefix and suffix max
        let mut pref = height.clone();
        let mut suff = height.clone();

        for i in 1..n {
            pref[i] = max(pref[i], pref[i-1]);
            suff[n-1-i] = max(suff[n-i], suff[n-1-i]);
        }

        // ignore first and last indices
        // as no water can be held here
        for i in 1..n-1 {
            water += min(pref[i], suff[i]) - height[i];
        }

        return water;
    }
}