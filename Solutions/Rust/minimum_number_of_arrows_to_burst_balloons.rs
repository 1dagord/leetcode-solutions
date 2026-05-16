/*
    [MEDIUM]
    452. Minimum Number of Arrows to Burst Balloons

    Concepts:
    - array
    - greedy
    - sorting

    Stats:
        Runtime | 19 ms     [Beats 72.73%]
        Memory  | 10.17 MB  [Beats 61.82%]
*/
use std::cmp::min;

impl Solution {
    pub fn find_min_arrow_shots(mut points: Vec<Vec<i32>>) -> i32 {
        /*
            Find number of overlaps in ranges

            1) sort intervals by start value
            2) check if start of current interval is before
                end of previous
            3) if above is true, overlap (decrement number of arrows)
        */
        points.sort();

        // max number of arrows is same as number of balloons
        let mut arrows: usize = points.len();
        let mut prev: Vec<i32> = points[0].clone();
        let mut curr: &Vec<i32>;
        let [mut s1, mut e1, mut s2, mut e2]: [i32; 4];

        for i in 1..points.len() {
            curr = &points[i as usize];
            [s1, e1] = [prev[0], prev[1]];
            [s2, e2] = [curr[0], curr[1]];

            // if overlap found, decrement number of arrows
            if s2 <= e1 {
                arrows -= 1;
                [prev[0], prev[1]] = [s2, min(e1, e2)];
            }

            // otherwise, update previous interval
            else { [prev[0], prev[1]] = [curr[0], curr[1]]; }
        }

        return arrows as i32;
    }
}