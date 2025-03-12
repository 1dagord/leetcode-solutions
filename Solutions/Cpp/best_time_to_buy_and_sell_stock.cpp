/*
    [EASY]
    121. Best Time to Buy and Sell Stock

    Concepts:
    - array

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 97.17 MB  [Beats 99.07%]
*/

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max_profit = 0;
        u_short min_price = std::numeric_limits<u_short>::max();

        for (const u_short price : prices) {
            if (price < min_price)
                min_price = price;
            if (price - min_price > max_profit)
                max_profit = price - min_price;
        }
        return max_profit;
    }
};