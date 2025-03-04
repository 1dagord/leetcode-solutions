"""
    [MEDIUM]
    909. Snakes and Ladders

    Concepts:
    - matrix
    - breadth-first search

    Stats:
        Runtime | 24 ms     [Beats 47.52%]
        Memory  | 17.96 MB  [Beats 59.05%]
"""

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        min_rolls = float("inf")
        n_squared = n ** 2

        def to_coords(idx: int) -> tuple[int]:
            return (
                (n - 1 - (idx // n)),
                (n - 1 - (idx % n))
                if (idx // n) & 1
                else (idx % n)
            )

        # convert indices to boustrophedon coordinates
        idx_to_coords, coords_to_idx = {}, {}
        for i in range(n_squared):
            idx_to_coords[i+1] = to_coords(i)
            coords_to_idx[to_coords(i)] = i+1
        
        # explore board
        def bfs():
            queue = deque([(1, 0)])  # idx, moves
            visited = set([1])

            while queue:
                len_q = len(queue)

                for _ in range(len_q):
                    idx, moves = queue.popleft()

                    if idx == n_squared:
                        return moves

                    for didx in reversed(range(1, 7)):
                        nidx = idx + didx
                        if nidx > n_squared:
                            continue

                        i, j = idx_to_coords[nidx]
                        if board[i][j] != -1:
                            nidx = board[i][j]

                        if nidx not in visited:
                            queue.append((nidx, moves + 1))
                            visited.add(nidx)

            return -1

        return bfs()