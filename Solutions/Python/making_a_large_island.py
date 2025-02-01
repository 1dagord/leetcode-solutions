"""
    [HARD]
    827. Making A Large Island

    Concepts:
    - matrix
    - depth-first search

    Stats:
        Runtime | 1531 ms   [Beats 17.85%]
        Memory  | 117.68 MB [Beats 5.04%]
"""

from collections import defaultdict

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        islands = defaultdict(int)  # id |-> size
        visited = set()

        def is_in_bounds(i, j) -> bool:
            return (0 <= i < n and 0 <= j < n)

        def dfs(i, j, island_id):
            nonlocal visited
            visited.add((i, j))

            if not grid[i][j]:
                return 0

            grid[i][j] = island_id

            size = 1
            for di, dj in moves:
                ni, nj = i + di, j + dj
                if is_in_bounds(ni, nj) and (ni, nj) not in visited:
                    size += dfs(ni, nj, island_id)

            return size

        # get island sizes
        island_id = 1
        for i in range(n):
            for j in range(n):
                if grid[i][j] and (i, j) not in visited:
                    islands[island_id] = dfs(i, j, island_id)

                    island_id += 1

        def join(i, j) -> int:
            # join all adjacent islands
            id_set = set()
            for di, dj in moves:
                ni, nj = i + di, j + dj
                if is_in_bounds(ni, nj):
                    id_set.add(grid[ni][nj])

            return 1 + sum([islands[num] for num in id_set])

        # join all available islands
        res = 0 if not islands else max(islands.values())
        for i in range(n):
            for j in range(n):
                if not grid[i][j]:
                    res = max(res, join(i, j))
        
        return res