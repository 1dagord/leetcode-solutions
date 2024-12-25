"""
    [MEDIUM]
    200. Number of Islands

    Concepts:
    - matrix
    - breadth-first search

    Stats:
        Runtime | 275 ms    [Beats 24.79%]
        Memory  | 26.49 MB  [Beats 15.15%]
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
            Iterate over every cell

            When land found, run BFS
            on cell until water reached

            When finished, increment number of islands
        """
        m, n = len(grid), len(grid[0])
        num_islands = 0
        explored = set()

        def bfs(y: int, x: int) -> set:
            nonlocal explored

            queue = deque([(y, x)])
            visited = set()

            while queue:
                len_queue = len(queue)

                for _ in range(len_queue):
                    i, j = queue.popleft()

                    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        if (0 <= (ni := i + di) < m and
                            0 <= (nj := j + dj) < n and
                            grid[ni][nj] == "1" and
                            (ni, nj) not in visited):

                            queue.append((ni, nj))
                            visited.add((ni, nj))

            return visited

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in explored:
                    explored.update(bfs(i, j))
                    num_islands += 1

        return num_islands