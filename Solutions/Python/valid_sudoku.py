"""
    [MEDIUM]
    36. Valid Sudoku

    Concepts:
    - matrix
    - hash table

    Stats:
        Runtime | 3 ms      [Beats 83.02%]
        Memory  | 16.64 MB  [Beats 100%]
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowVisited = set()
        colVisited = set()
        boxVisited = set()

        for i in range(9):
            for j in range(9):
                row = ((3 * (i%3) + (j//3)) % 3) + 3*((j + i*9)//27)
                col = j%3 + 3*(i%3)

                if (board[i][j] in rowVisited and board[i][j] != "." or
                    board[j][i] in colVisited and board[j][i] != "." or
                    board[row][col] in boxVisited and board[row][col] != "."):
                    return False

                rowVisited.add(board[i][j])
                colVisited.add(board[j][i])
                boxVisited.add(board[row][col])

            rowVisited.clear()
            colVisited.clear()
            boxVisited.clear()

        return True