/*
    [HARD]
    52. N-Queens II

    Concepts:
    - backtracking

    Stats:
        Runtime | 8 ms      [Beats 13.05%]
        Memory  | 10.53 MB  [Beats 9.69%]
*/

class Solution {
public:
    int totalNQueens(int n) {
        int count = 0;
        std::unordered_set<int> used_cols = {};
        std::unordered_set<int> diags = {};
        std::unordered_set<int> antidiags = {};

        std::function<void(int)> backtrack;
        backtrack = [&](int i){
            if (i == n) {
                count++;
                return;
            }

            for (int j = 0; j < n; j++) {
                if (
                    used_cols.contains(j) ||
                    diags.contains(i + j) ||
                    antidiags.contains(i - j)
                ) {
                    continue;
                }

                used_cols.insert(j);
                diags.insert(i + j);
                antidiags.insert(i - j);

                backtrack(i + 1);

                used_cols.erase(j);
                diags.erase(i + j);
                antidiags.erase(i - j);
            }

            return;
        };

        backtrack(0);
        return count;
    }
};