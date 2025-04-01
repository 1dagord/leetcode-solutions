/*
    [MEDIUM]
    77. Combinations

    Concepts:
    - backtracking

    Stats:
        Runtime | 50 ms     [Beats 48.13%]
        Memory  | 63.73 MB  [Beats 47.67%]
*/

class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        std::vector<std::vector<int>> res = {};
        std::vector<int> path = {};

        std::function<void(int)> dfs;
        dfs = [&](int num){
            if (path.size() == k)
                return res.push_back(path);

            for (int i = num; i <= n; i++) {
                path.push_back(i);
                dfs(i + 1);
                path.pop_back();
            }
        };

        dfs(1);
        return res;
    }
};