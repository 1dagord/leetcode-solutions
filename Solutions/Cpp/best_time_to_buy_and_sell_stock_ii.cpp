/*
    [MEDIUM]
    122. Best Time to Buy and Sell Stock II

    Concepts:
    - array
    - greedy

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 17.06 MB  [Beats 84.11%]
*/

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max_profit = 0;
        u_short yesterday = prices[0];

        for (const u_short today : prices) {
            if (yesterday < today)
                max_profit += today - yesterday;
            yesterday = today;
        }
        return max_profit;
    }
};