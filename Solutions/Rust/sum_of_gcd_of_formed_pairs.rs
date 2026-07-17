/*
    [MEDIUM]
    3867. Sum of GCD of Formed Pairs

    Concepts:
    - array
    - simulation

    Stats:
        Runtime | 47 ms     [Beats 46.05%]
        Memory  | 5.27 MB   [Beats 7.44%]
*/
use std::cmp::max;

impl Solution {
    pub fn gcd_sum(arr: Vec<i32>) -> i64 {
        let nums: Vec<i64> = arr.into_iter().map(|v| v as i64).collect();
        let mut pref: Vec<i64> = Vec::new();
        let mut maxes: Vec<i64> = nums.clone();
        let mut sum: i64 = 0;

        fn gcd(a: i64, b: i64) -> i64 {
            if b == 0 {
                return a;
            }
            return gcd(b, a % b);
        }

        for i in 0..nums.len() {
            if i > 0 {
                maxes[i] = max(maxes[i - 1], nums[i]);
            }
            pref.push(if nums[i] < maxes[i] {
                gcd(nums[i], maxes[i])
            } else {
                gcd(maxes[i], nums[i])
            });
        }

        pref.sort();
        let n = pref.len();
        for i in 0..n / 2 {
            sum += gcd(pref[i], pref[n - 1 - i]);
        }

        return sum;
    }
}
