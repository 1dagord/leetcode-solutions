/*
    [MEDIUM]
    64. Minimum Path Sum

    Concepts:
    - matrix
    - dynamic programming

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 16.17 MB  [Beats 68.32%]
*/

class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        const int m = grid.size(), n = grid[0].size();
        std::vector<std::vector<int>> dp(
            m,
            std::vector<int>(
                n,
                std::numeric_limits<int>::infinity()
            )
        );

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i && j)
                    dp[i][j] = grid[i][j] + std::min(dp[i-1][j], dp[i][j-1]);
                else if (i && !j)
                    dp[i][0] = dp[i-1][0] + grid[i][0];
                else if (j && !i)
                    dp[0][j] = dp[0][j-1] + grid[0][j];
                else
                    dp[0][0] = grid[0][0];
            }
        }

        return dp.back().back();
    }
};