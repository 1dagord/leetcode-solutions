/*
    [MEDIUM]
    36. Valid Sudoku

    Concepts:
    - matrix
    - hash table

    Stats:
        Runtime | 3 ms      [Beats 15.48%]
        Memory  | 2.21 MB   [Beats 45.24%]
*/
use std::collections::HashSet;

impl Solution {
    pub fn is_valid_sudoku(board: Vec<Vec<char>>) -> bool {
        let mut row_visited: HashSet<char> = HashSet::new();
        let mut col_visited: HashSet<char> = HashSet::new();
        let mut box_visited: HashSet<char> = HashSet::new();
        let [mut row, mut col]: [usize; 2];

        for i in 0..9 {
            for j in 0..9 {
                row = ((3 * (i%3) + (j/3)) % 3) + 3*((j + i*9) / 27);
                col = (j%3) + (3*(i%3));

                if (
                    row_visited.contains(&board[i][j]) && board[i][j] != '.'
                    || col_visited.contains(&board[j][i]) && board[j][i] != '.'
                    || box_visited.contains(&board[row][col]) && board[row][col] != '.'
                ) {
                    return false;
                }

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
}