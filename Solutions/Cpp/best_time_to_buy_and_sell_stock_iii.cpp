/*
    [HARD]
    123. Best Time to Buy and Sell Stock III

    Concepts:
    - array
    - dynamic programming

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 79.25 MB  [Beats 87.43%]
*/

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        const long INF = std::numeric_limits<long>::max();

        // initialize variables for first buy, first sell,
        // second buy, and second cell
        long buy1 = INF, buy2 = INF;
        long sell1 = 0, sell2 = 0;

        // iterate over prices to update buy and sell values
        for (const long price : prices) {
            // update first buy and sell values
            buy1 = std::min(buy1, price);
            sell1 = std::max(sell1, price - buy1);
            // update second buy and sell values
            buy2 = std::min(buy2, price - sell1);
            sell2 = std::max(sell2, price - buy2);
        }

        return (int)sell2;
    }
};