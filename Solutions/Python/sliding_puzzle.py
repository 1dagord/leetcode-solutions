"""
    [HARD]
    773. Sliding Puzzle

    Concepts:
    - matrix
    - breadth-first search

    Stats:
        Runtime | 39 ms     [Beats 20.11%]
        Memory  | 16.78 MB  [Beats 53.43%]
"""

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        """
            Each board state is a node
            Every valid move is a child node (4 max)

            Construct tree until solution node reached
        """
        soln = ((1, 2, 3),
                (4, 5, 0))
        board = tuple([tuple(row) for row in board])

        def make_new_board(board: tuple, i: int, j: int, ni: int, nj: int) -> tuple:
            b = [[item for item in row] for row in board]
            b[i][j], b[ni][nj] = b[ni][nj], b[i][j]
            return tuple([tuple(row) for row in b])


        def bfs(row: int, col: int) -> int:
            states = deque()
            states.append(board)
            visited = set()
            moves = 0

            while states:
                n = len(states)

                for _ in range(n):
                    # current board state
                    curr = states.popleft()
                    visited.add(curr)

                    if curr == soln:
                        return moves

                    # find elements adjacent to zero
                    for i in range(2):
                        for j in range(3):

                            # check for valid unvisited board states
                            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:

                                if (0 <= (ni := i + di) < 2 and
                                    0 <= (nj := j + dj) < 3 and
                                    curr[ni][nj] == 0 and
                                    (new_board := make_new_board(curr, i, j, ni, nj)) not in visited):

                                    # explore new board state
                                    states.append(new_board)

                moves += 1

            return -1

        return bfs(0, 0)
