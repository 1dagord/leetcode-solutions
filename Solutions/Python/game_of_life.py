"""
    [MEDIUM]
    289. Game of Life

    Concepts:
    - matrix
    - simulation

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 17.80 MB  [Beats 25.41%]
"""

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        """
            < 2 live neighbors: dies
            2-3 live neighbors: survives
            >3 live neighbors: dies
            dead w 3 live neighbors: revived
        """
        m, n = len(board), len(board[0])

        next_state = [[item for item in row] for row in board]
        moves = [(x, y) for x in range(-1, 2) for y in range(-1, 2)]
        moves.remove((0, 0))

        # get next state
        for i in range(m):
            for j in range(n):

                # get number of live neighbors
                live_neighbors = 0
                for di, dj in moves:
                    if (0 <= (ni := i + di) < m and
                        0 <= (nj := j + dj) < n and
                        board[ni][nj]):
                        live_neighbors += 1

                # if current cell is live...
                if board[i][j]:
                    if (live_neighbors < 2 or
                        live_neighbors > 3):
                        next_state[i][j] = 0
                    elif (live_neighbors in [2, 3]):
                          next_state[i][j] = 1
                # if current cell is dead...
                else:
                    if live_neighbors == 3:
                        next_state[i][j] = 1

        # update board
        for i in range(m):
            board[i] = next_state[i]