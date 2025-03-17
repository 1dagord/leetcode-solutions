/*
    [MEDIUM]
    36. Valid Sudoku

    Concepts:
    - matrix
    - hash table

    Stats:
        Runtime | 3 ms      [Beats 63.12%]
        Memory  | 23.36 MB  [Beats 58.48%]
*/

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        std::unordered_set<char> row_visited = {};
        std::unordered_set<char> col_visited = {};
        std::unordered_set<char> box_visited = {};
        int row, col;

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                row = ((3 * (i%3) + (j/3)) % 3) + 3*((j + i*9) / 27);
                col = (j%3) + (3*(i%3));

                if (
                    (row_visited.contains(board[i][j]) && board[i][j] != '.') ||
                    (col_visited.contains(board[j][i]) && board[j][i] != '.') ||
                    (box_visited.contains(board[row][col]) && board[row][col] != '.')
                )
                    return false;

                row_visited.insert(board[i][j]);
                col_visited.insert(board[j][i]);
                box_visited.insert(board[row][col]);
            }

            row_visited.clear();
            col_visited.clear();
            box_visited.clear();
        }

        return true;
    }
};