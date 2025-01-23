"""
    [MEDIUM]
    1267. Count Servers that Communicate

    Concepts:
    - matrix
    - counting

    Stats:
        Runtime | 27 ms     [Beats 25.47%]
        Memory  | 19.68 MB  [Beats 35.58%]
"""

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rows = [0]*m
        cols = [0]*n
        count = 0

        # count computers in rows and columns
        for i in range(m):
            for j in range(n):
                rows[i] += grid[i][j]
                cols[j] += grid[i][j]

        # check each position for multiple
        # computers in same row/col
        for i in range(m):
            for j in range(n):
                if grid[i][j] and (rows[i] > 1 or cols[j] > 1):
                    count += 1

        return count