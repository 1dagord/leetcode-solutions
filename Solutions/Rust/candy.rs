/*
    [HARD]
    135. Candy

    Concepts:
    - array
    - greedy

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.32 MB   [Beats 55.00%]
*/
use std::cmp::max;

impl Solution {
    pub fn candy(ratings: Vec<i32>) -> i32 {
        let n: usize = ratings.len();
        let mut candies = Vec::with_capacity(n);
        let [mut lhn, mut rhn] = [0, 0];
        for _ in 0..n { candies.push(1); }

        // forward pass
        // if rating higher than LH neighbor, increment
        for i in 1..n {
            lhn = ratings[i-1];
            rhn = ratings[i];
            if lhn < rhn { candies[i] = 1 + candies[i-1]; }
        }

        // backward pass
        // if rating higher than RH neighbor, increment
        for i in (0..n-1).rev() {
            lhn = ratings[i];
            rhn = ratings[i+1];
            if lhn > rhn { candies[i] = max(candies[i], 1 + candies[i+1]); }
        }

        return candies.into_iter().fold(0, |a, b| a + b);
    }
}