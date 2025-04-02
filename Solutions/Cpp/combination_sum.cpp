/*
    [MEDIUM]
    39. Combination Sum

    Concepts:
    - backtracking

    Stats:
        Runtime | 4 ms      [Beats 43.79%]
        Memory  | 15.21 MB  [Beats 38.85%]
*/

class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& cands, int target) {
        std::vector<std::vector<int>> combos = {};
        std::vector<int> path = {};
        std::sort(cands.begin(), cands.end());

        std::function<void(int, int)> dfs;
        dfs = [&](int idx, int curr){
            if (curr == target)
                combos.push_back(path);
            else if (curr > target)
                return;

            for (int i = idx; i < cands.size(); i++) {
                if (curr < target) {
                    path.push_back(cands[i]);
                    dfs(i, curr + cands[i]);
                    path.pop_back();
                }
            }
        };

        dfs(0, 0);
        return combos;
    }
};