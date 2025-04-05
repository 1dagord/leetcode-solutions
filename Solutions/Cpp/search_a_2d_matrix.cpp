/*
    [MEDIUM]
    74. Search a 2D Matrix

    Concepts:
    - matrix
    - binary search

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 13.30 MB  [Beats 76.86%]
*/

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m, n, left, mid, right;
        m = matrix.size(), n = matrix[0].size();
        left = 0, right = m * n - 1;

        while (left <= right) {
            mid = (left + right) / 2;

            if (matrix[mid / n][mid % n] < target)
                left = mid + 1;
            else if (matrix[mid / n][mid % n] > target)
                right = mid - 1;
            else
                return true;
        }

        return false;
    }
};