/*
    [EASY]
    3658. GCD of Odd and Even Sums

    Concepts:
    - math
    - number theory

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.23 MB   [Beats 3.45%]
*/
use std::cmp::{max, min};

impl Solution {
    pub fn gcd_of_odd_even_sums(n: i32) -> i32 {
        let num_odd = n.pow(2);
        let num_even = n * (n + 1);

        fn gcd(small: i32, large: i32) -> i32 {
            if small == large {
                return large;
            }

            return gcd(min(large - small, small), max(large - small, small));
        }

        return gcd(min(num_odd, num_even), max(num_odd, num_even));
    }
}
