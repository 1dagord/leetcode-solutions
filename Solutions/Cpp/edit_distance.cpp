/*
    [MEDIUM]
    72. Edit Distance

    Concepts:
    - string
    - dynamic programming
    
    Stats:
        Runtime | 4 ms      [Beats 80.30%]
        Memory  | 12.93 MB  [Beats 73.77%]
*/

class Solution {
public:
    int minDistance(string w1, string w2) {
        /*
            Imagine 2D matrix where chars of word1
            are along column and chars of word2 are
            along rows
        */
        const int m = w1.size(), n = w2.size();
        std::vector<std::vector<int>> dp(
            m+1,
            std::vector<int>(
                n+1,
                std::numeric_limits<int>::infinity()
            )
        );

        // initialize empty rows and cols for case
        // when either string is empty
        for (int j = 0; j <= n; j++)
            dp[m][j] = n - j;
        for (int i = 0; i <= m; i++)
            dp[i][n] = m - i;

        for (int i = m - 1; i > -1; i--) {
            for (int j = n - 1; j > -1; j--) {
                if (w1[i] == w2[j])
                    dp[i][j] = dp[i+1][j+1];
                else
                    dp[i][j] = 1 + std::min(
                        std::min(
                            dp[i+1][j],     // delete
                            dp[i][j+1]      // insert
                        ),
                        dp[i+1][j+1]        // replace
                    );
            }
        }

        return dp[0][0];
    }
};