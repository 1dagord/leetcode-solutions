"""
    [HARD]
    2290. Minimum Obstacle Removal to Reach Corner

    Concepts:
    - matrix
    - breadth-first search
    - shortest path

    Stats:
        Runtime | 976 ms    [Beats 67.96%]
        Memory  | 47.46 MB  [Beats 16.61%]
"""

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        """
            0-1 BFS: Shortest Path in Binary Weighted Graph

            Typical BFS, except node weight influences order in deque

            If node has weight 0, prepend to deque
            Else, append to deque
        """
        m, n = len(grid), len(grid[0])
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # (x, y, num_removed)
        dq = deque([(0, 0, 0)])
        visited = set((0, 0))
        
        while dq:
            i, j, num_removed = dq.popleft()
            
            # if reached bottom right corner...
            if i == m - 1 and j == n - 1:
                return num_removed
            
            for di, dj in moves:                
                if (0 <= (ni := i + di) < m and
                    0 <= (nj := j + dj) < n and
                    (ni, nj) not in visited):

                    visited.add((ni, nj))
                    # if no obstacle to remove...
                    if grid[ni][nj] == 0:
                        # ...continue down current path
                        dq.appendleft((ni, nj, num_removed))
                    else:
                        # ...remove obstacle
                        dq.append((ni, nj, num_removed + 1))
        
        # if no path exists...
        return -1