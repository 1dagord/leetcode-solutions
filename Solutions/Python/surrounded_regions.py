"""
    [MEDIUM]
    130. Surrounded Regions

    Concepts:
    - matrix
    - depth-first search

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 21.76 MB  [Beats 58.50%]
"""

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        placeholder = 1

        def is_on_edge(i: int, j: int) -> bool:
            return i == 0 or j == 0 or i == m-1 or j == n-1

        def dfs(i: int, j: int) -> None:
            board[i][j] = placeholder
            for di, dj in moves:
                if (0 <= (ni := i + di) < m and
                    0 <= (nj := j + dj) < n and
                    board[ni][nj] == "O"):
                    dfs(ni, nj)

        # perform dfs from only "O"s on edges
        for i in range(m):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][n-1] == "O":
                dfs(i, n-1) 

        for j in range(n):
            if board[0][j] == "O":
                dfs(0, j)
            if board[m-1][j] == "O":
                dfs(m-1, j)

        # set every non-explored "O" to an "X"
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == placeholder:
                    board[i][j] = "O"