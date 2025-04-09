/*
    [HARD]
    502. IPO

    Concepts:
    - array
    - greedy
    - heap/priority queue

    Stats:
        Runtime | 104 ms    [Beats 28.63%]
        Memory  | 131.30 MB [Beats 74.32%]
*/

class Solution {
public:
    int findMaximizedCapital(int k, int money, vector<int>& profits, vector<int>& capital) {
        std::priority_queue<int> max_prof = {};
        std::priority_queue<
            std::pair<int, int>,
            std::vector<std::pair<int, int>>,
            std::greater<std::pair<int, int>>
        > min_cap = {};

        for (int i = 0; i < profits.size(); i++)
            min_cap.emplace(capital[i], profits[i]);

        for (int _ = 0; _ < k; _++) {
            // push all affordable projects to max heap 'min_prof'
            while (!min_cap.empty() && min_cap.top().first <= money) {
                max_prof.push(min_cap.top().second);
                min_cap.pop();
            }

            // if no affordable projects...
            if (max_prof.empty())
                break;

            // complete most profitable project
            money += max_prof.top(); max_prof.pop();
        }

        return money;
    }
};