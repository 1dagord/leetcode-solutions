/*
    [HARD]
    188. Best Time to Buy and Sell Stock IV
    
    Concepts:
    - array
    - dynamic programming

    Stats:
        Runtime | 482 ms    [Beats 5.01%]
        Memory  | 80.83 MB  [Beats 6.21%1]
*/

class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        const int n = prices.size();
        std::unordered_map<std::string, int> cache = {};

        std::function<int(int, int, bool)> transact;
        transact = [&](int date, int limit, bool is_buying){
            if (limit == 0 || date == n)
                return 0;

            std::string state = std::to_string(date) + "," + std::to_string(limit) + "," + std::string{is_buying};

            if (cache.contains(state))
                return cache[state];

            if (is_buying) {
                // either buy today or wait to buy another day
                cache[state] = std::max(
                    transact(date + 1, limit, false) - prices[date],
                    transact(date + 1, limit, true)
                );
            } else {
                cache[state] = std::max(
                    transact(date + 1, limit - 1, true) + prices[date],
                    transact(date + 1, limit, false)
                );
            }

            return cache[state];
        };

        return transact(0, k, true);
    }
};