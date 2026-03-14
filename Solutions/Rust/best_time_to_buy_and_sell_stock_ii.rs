/*
    [MEDIUM]
    122. Best Time to Buy and Sell Stock II

    Concepts:
    - array
    - greedy

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.30 MB   [Beats 28.72%%]
*/

impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut max_profit: i32 = 0;
        let mut yesterday: i32 = prices[0];

        for today in prices {
            if yesterday < today {
                max_profit += today - yesterday;
            }
            yesterday = today;
        }

        return max_profit;
    }
}