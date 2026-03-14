/*
    [EASY]
    121. Best Time to Buy and Sell Stock

    Concepts:
    - array

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.87 MB   [Beats 98.93%]
*/

impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut max_profit = 0;
        let mut min_price = (10 as i32).pow(8) + 1;

        for price in prices {
            if price < min_price {
                min_price = price;
            }
            if price - min_price > max_profit {
                max_profit = price - min_price;
            }
        }

        return max_profit;
    }
}