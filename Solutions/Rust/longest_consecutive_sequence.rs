/*
    [MEDIUM]
    128. Longest Consecutive Sequence

    Concepts:
    - array
    - hash table

    Stats:
        Runtime | 17 ms     [Beats 44.50%]
        Memory  | 3.64 MB   [Beats 71.77%]
*/
use std::collections::BTreeSet;
use std::cmp::max;

impl Solution {
    pub fn longest_consecutive(nums: Vec<i32>) -> i32 {
        let mut length: i32 = 0;
        let mut vals: BTreeSet<i32> = BTreeSet::from_iter(nums);
        let [mut val, mut lo, mut hi]: [i32; 3];

        while !vals.is_empty() {
            val = vals.pop_first().unwrap();

            [lo, hi] = [val, val];
            while vals.contains(&(lo - 1)) {
                vals.remove(&(lo - 1));
                lo -= 1;
            }
            while vals.contains(&(hi + 1)) {
                vals.remove(&(hi + 1));
                hi += 1;
            }

            length = max(hi - lo + 1, length);
        }

        return length;
    }
}