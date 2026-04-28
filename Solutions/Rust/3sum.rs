/*
    [MEDIUM]
    15. 3Sum

    Concepts:
    - two pointers
    - sorting

    Stats:
        Runtime | 19 ms     [Beats 56.95%]
        Memory  | 3.71 MB   [Beats 96.57%]
*/
use std::collections::HashSet;

impl Solution {
    pub fn three_sum(mut nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut triplets = HashSet::new();
        nums.sort();

        let n = nums.len();
        let [mut target, mut val]: [i32; 2] = [0, 0];
        let [mut j, mut k]: [usize; 2] = [0, 0];

        for i in 0..n {
            if i != 0 && nums[i] == nums[i-1] {
                continue;
            }

            target = -nums[i];

            j = i + 1;
            k = n - 1;

            while j < k {
                val = nums[j] + nums[k];

                if val == target {
                    triplets.insert([nums[i], nums[j], nums[k]]);

                    j += 1;
                    k -= 1;
                } else if val > target {
                    k -= 1;
                } else {
                    j += 1;
                }
            }

        }

        return triplets
            .into_iter()
            .map(|item| Vec::from(item))
            .collect::<Vec<Vec<i32>>>();
    }
}