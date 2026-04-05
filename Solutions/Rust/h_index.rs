/*
    [MEDIUM]
    274. H-Index

    Concepts:
    - sorting
    - counting sort

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.16 MB   [Beats 84.62%]
*/
use std::cmp::min;
use std::cmp::max;

impl Solution {
    pub fn h_index(mut citations: Vec<i32>) -> i32 {
        citations.sort_by(|a, b| b.cmp(a));
        let mut h_index: i32 = 0;
        let mut num_papers_w_cit: i32 = 0;

        for i in 0..citations.len() {
            num_papers_w_cit = i as i32 + 1;
            h_index = max(h_index, min(num_papers_w_cit, citations[i]));
        }

        return h_index;
    }
}