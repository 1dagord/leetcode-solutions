/*
    [MEDIUM]
    48. Rotate Image

    Concepts:
    - matrix
    - math

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 10.34 MB  [Beats 8.64%]
*/

class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();
        std::vector<std::vector<int>> rot_mat(n, std::vector(n, -1));

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++)
                rot_mat[j][n-i-1] = matrix[i][j];
        }

        matrix = rot_mat;
    }
};