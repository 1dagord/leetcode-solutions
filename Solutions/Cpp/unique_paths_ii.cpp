/*
    [MEDIUM]
    63. Unique Paths II

    Concepts:
    - matrix
    - dynamic programming

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 15.80 MB  [Beats 6.57%]
*/

class Solution {
public:
    int m, n;

    inline int coords_to_idx(const int i, const int j) {
        return (i * n) + (j % n);
    }

    int uniquePathsWithObstacles(vector<vector<int>>& grid) {
        m = grid.size(), n = grid[0].size();
        std::unordered_map<int, int> dp = {};

        if (m == 1 && n == 1)
            return !grid[0][0];

        if (grid[0][0])
            return 0;

        std::function<int(int, int)> dfs;
        dfs = [&](int i, int j){
            int idx = coords_to_idx(i, j);

            if (i == m - 1 && j == n - 1) {
                dp[idx] = 1;
                return dp[idx];
            }

            if (dp.contains(idx))
                return dp[idx];

            if (i + 1 < m && !grid[i+1][j])
                dp[idx] += dfs(i + 1, j);
            if (j + 1 < n && !grid[i][j+1])
                dp[idx] += dfs(i, j + 1);

            return dp[idx];
        };

        return dfs(0, 0);
    }
};