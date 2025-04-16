/*
    [MEDIUM]
    221. Maximal Square

    Concepts:
    - matrix
    - dynamic programming

    Stats:
        Runtime | 16 ms     [Beats 26.06%]
        Memory  | 34.16 MB  [Beats 6.81%]
*/

class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        const int m = matrix.size(), n = matrix[0].size();
        std::vector<std::vector<int>> dp(m+1, std::vector<int>(n+1, 0));
        std::array<int, 3> neighbors = {};

        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                dp[i][j] = matrix[i][j] - '0';

        for (int i = m - 1; i > -1; i--) {
            for (int j = n - 1; j > -1; j--) {
                neighbors = std::array<int, 3>{
                    dp[i+1][j],
                    dp[i][j+1],
                    dp[i+1][j+1]
                };

                if (dp[i][j] != 0 && std::accumulate(neighbors.begin(), neighbors.end(), 0) >= 3)
                    dp[i][j] += *std::min_element(neighbors.begin(), neighbors.end());
            }
        }

        int res = 0;
        for (std::vector<int> row : dp)
            for (int val : row)
                res = std::max(res, val);

        return std::pow(res, 2);
    }
};