/*
    [MEDIUM]
    73. Set Matrix Zeroes

    Concepts:
    - matrix

    Stats:
        Runtime | 3 ms      [Beats 11.45%]
        Memory  | 19.38 MB  [Beats 7.13%]
*/

class Solution {
public:
    void setZeroes(vector<vector<int>>& A) {
        uint8_t m = A.size(), n = A[0].size();
        double sentinel = std::pow(2, 31);

        std::vector<std::vector<double>> matrix(m, std::vector(n, 0.0));
        for (uint8_t i = 0; i < m; i++) {
            for (uint8_t j = 0; j < n; j++) {
                matrix[i][j] = A[i][j];
            }
        }

        // set marked elements to `sentinel`
        for (uint8_t i = 0; i < m; i++) {
            for (uint8_t j = 0; j < n; j++) {
                if (matrix[i][j] != sentinel && matrix[i][j] == 0) {
                    for (uint8_t row = 0; row < m; row++) {
                        if (row != i && matrix[row][j] != 0)
                            matrix[row][j] = sentinel;
                    }
                    for (uint8_t col = 0; col < n; col++) {
                        if (col != j && matrix[i][col] != 0)
                            matrix[i][col] = sentinel;
                    }
                }
            }
        }

        // set `sentinel` elements to 0
        for (uint8_t i = 0; i < m; i++) {
            for (uint8_t j = 0; j < n; j++) {
                if (matrix[i][j] == sentinel)
                    A[i][j] = 0;
                else
                    A[i][j] = static_cast<int>(matrix[i][j]);
            }
        }
    }
};