/*
    [MEDIUM]
    46. Permutations

    Concepts:
    - backtracking

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 11.01 MB  [Beats 30.51%]
*/

class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        std::vector<std::vector<int>> perms = {};

        std::function<void(int)> backtrack;
        backtrack = [&](int idx){
            if (idx == nums.size())
                return perms.push_back({nums});

            for (int i = idx; i < nums.size(); i++) {
                std::swap(nums[i], nums[idx]);
                backtrack(idx + 1);
                std::swap(nums[i], nums[idx]);
            }
        };

        backtrack(0);
        return perms;
    }
};