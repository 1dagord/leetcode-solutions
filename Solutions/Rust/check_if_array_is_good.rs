/*
    [EASY]
    2784. Check if Array is Good

    Concepts:
    - array
    - hash table

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.16 MB   [Beats 80.00%]
*/
use std::collections::HashMap;

impl Solution {
    pub fn is_good(mut nums: Vec<i32>) -> bool {
        let max_num: i32 = *nums.iter().max().unwrap();
        let mut base_n: Vec<i32> = (1..=max_num).collect::<Vec<i32>>();
        base_n.push(max_num);
        let mut perm: HashMap<i32, i32> = HashMap::new();
        base_n
            .iter()
            .for_each(|&num| {
                perm
                    .entry(num)
                    .and_modify(|v| *v += 1)
                    .or_insert(1);
            });

        for num in nums {
            perm
                .entry(num)
                .and_modify(|v| *v -= 1);

            if perm.get(&num).is_some() {
                if *perm.get(&num).unwrap() == 0 { perm.remove(&num); }
            } else {
                return false;
            }
        }

        return perm.is_empty();
    }
}