/*
    [MEDIUM]
    322. Coin Change

    Concepts:
    - dynamic programming
    - breadth-first search

    Stats:
        Runtime | 19 ms     [Beats 80.41%]
        Memory  | 17.56 MB  [Beats 93.83%]
*/

class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        /*
            BFS
        */
        // amount -> is_visited
        std::vector<bool> visited(amount + 1, false);
        std::deque<int> q;
        q.push_back(amount);

        int level = 0; // tracks the number of coins used (BFS level)
        int q_size, curr_amount, new_amount;

        while (!q.empty()) {
            // number of elements at the current level
            q_size = q.size();

            // explore nodes at the current level
            for (int _ = 0; _ < q_size; _++) {
                curr_amount = q.front();
                q.pop_front();

                if (curr_amount == 0)
                    return level;

                // check next amounts by using available coins
                for (const int coin : coins) {
                    new_amount = curr_amount - coin;
                    if (new_amount >= 0 && !visited[new_amount]) {
                        q.push_back(new_amount);
                        visited[new_amount] = true;
                    }
                }
            }

            level++;
        }

        return -1; // if BFS is exhausted without reaching amount 0
    }
};