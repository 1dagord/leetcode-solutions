"""
    [MEDIUM]
    1765. Map of Highest Peak

    Concepts:
    - matrix
    - breadth-first search

    Stats:
        Runtime | 742 ms    [Beats 75.06%]
        Memory  | 85.00 MB  [Beats 53.88%]
"""

from collections import deque

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        """
            Perform BFS from every water cell
        """
        m, n = len(isWater), len(isWater[0])
        ground = [[-1]*n for _ in range(m)]

        # stores coordinates of water cells
        queue = deque()
        for i in range(m):
            for j in range(n):
                if isWater[i][j]:
                    queue.append((i, j, 0))
                    ground[i][j] = 0

        # bfs
        while queue:
            i, j, height = queue.popleft()

            # check all possible moves
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if (0 <= (ni := i + di) < m and
                    0 <= (nj := j + dj) < n and
                    ground[ni][nj] == -1):

                    queue.append((ni, nj, height + 1))
                    ground[ni][nj] = height + 1

        return ground
