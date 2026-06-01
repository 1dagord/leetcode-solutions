/*
    [EASY]
    2144. Minimum Cost of Buying Candies With Discount

    Concepts:
    - array
    - greedy

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.23 MB   [Beats 41.18%]
*/
impl Solution {
    pub fn minimum_cost(mut candies: Vec<i32>) -> i32 {
        candies.sort();
        let mut min_cost: i32 = 0;

        while !candies.is_empty() {
            if let Some(one) = candies.pop() {
                min_cost += one;
                if let Some(two) = candies.pop() {
                    min_cost += two;
                }
                candies.pop();
            }
        }

        return min_cost;
    }
}
