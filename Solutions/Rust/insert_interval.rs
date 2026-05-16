/*
    [MEDIUM]
    57. Insert Interval

    Concepts:
    - array

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.77 MB   [Beats 36.23%]
*/
use std::cmp::max;

impl Solution {
    pub fn insert(mut intervals: Vec<Vec<i32>>, new_interval: Vec<i32>) -> Vec<Vec<i32>> {
        intervals.push(new_interval);
        intervals.sort();

        let mut res: Vec<Vec<i32>> = Vec::new();

        for intv in intervals {
            if let Some(res_last) = res.last_mut() {
                // compare last interval's end with current interval's *start*
                if res_last[1] >= intv[0] {
                    // compare last interval's end with current interval's *end*
                    res_last[1] = max(res_last[1], intv[1]);
                    continue;
                }
            }
            // if no overlap between last and current, create new interval
            res.push(intv.clone());
        }

        return res;
    }
}