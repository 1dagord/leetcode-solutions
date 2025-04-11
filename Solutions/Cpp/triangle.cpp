/*
    [MEDIUM]
    120. Triangle

    Concepts:
    - array
    - dynamic programming

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 12.46 MB  [Beats 92.21%]
*/

class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        // tabulation
        int min_sum;

        for (int i = triangle.size() - 2; i > -1; i--) {
            for (int j = 0; j < triangle[i].size(); j++) {
                min_sum = std::min(triangle[i + 1][j], triangle[i + 1][j + 1]);
                triangle[i][j] += min_sum;
            }
        }

        return triangle[0][0];
    }
};