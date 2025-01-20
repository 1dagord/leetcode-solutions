"""
    [HARD]
    1368. Minimum Cost to Make at Least One Valid Path in a Grid

    Concepts:
    - matrix
    - breadth-first search
    - heap/priority queue

    Stats:
        Runtime | 167 ms    [Beats 35.14%]
        Memory  | 19.92 MB  [Beats 33.43%]
"""

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        """
            0-1 BFS Approach

            Cost of moving to a neighboring cell
            is 0 if move is along arrow and
            1 otherwise
        """
        m, n = len(grid), len(grid[0])
        moves = {
            1 : (0, 1),
            2 : (0, -1),
            3 : (1, 0),
            4 : (-1, 0)
        }

        queue = deque([(0, 0, 0)])  # i, j, cost
        min_cost = {(0, 0) : 0}     # coords -> min cost (if cell visited)

        while queue:
            len_q = len(queue)

            for _ in range(len_q):
                i, j, cost = queue.popleft()

                if (i, j) == (m - 1, n - 1):
                    return cost

                for k, (di, dj) in moves.items():
                    # cost to move to neighbor
                    ncost = cost if grid[i][j] == k else cost + 1

                    if (0 <= (ni := i + di) < m and
                        0 <= (nj := j + dj) < n and
                        ncost < min_cost.get((ni, nj), float("inf"))):

                        # update min_cost
                        min_cost[(ni, nj)] = ncost

                        # if arrow points in direction of neighbor...
                        if grid[i][j] == k:
                            queue.appendleft((ni, nj, ncost))
                        else:
                            queue.append((ni, nj, ncost))