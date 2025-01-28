"""
    [MEDIUM]
    2658. Maximum Number of Fish in a Grid

    Concepts:
    - matrix
    - breadth-first search

    Stats:
        Runtime | 46 ms     [Beats 44.88%]
        Memory  | 17.88 MB  [Beats 63.41%]
"""

from collections import deque

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        """
            Number of islands, but return sum of
            cells in most valuable island
        """
        m, n = len(grid), len(grid[0])
        max_fish = 0

        def bfs(row: int, col: int) -> int:
            queue = deque([(row, col)])
            visited = set()
            total = 0

            while queue:
                i, j = queue.popleft()
                visited.add((i, j))
                total += grid[i][j]

                for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if (0 <= (ni := i + di) < m and
                        0 <= (nj := j + dj) < n and
                        (ni, nj) not in visited and
                        (ni, nj) not in queue and
                        grid[ni][nj]):
                        queue.append((ni, nj))

            return total, visited

        explored = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] and (i, j) not in explored:
                    fish, cells = bfs(i, j)
                    max_fish = max(fish, max_fish)
                    explored.update(cells)

        return max_fish