"""
    [HARD]
    2503. Maximum Number of Points From Grid Queries

    Concepts:
    - matrix
    - heap/priority queue
    - breadth-first search

    Stats:
        Runtime | 594 ms    [Beats 66.67%]
        Memory  | 43.21 MB  [Beats 13.72%]
"""

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])

        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ans = [0]*len(queries)

        sorted_queries = sorted([(q, i) for i, q in enumerate(queries)])

        count = 0
        visited = set([(0, 0)])
        heap = [(grid[0][0], 0, 0)] # val, i, j

        for query, idx in sorted_queries:
            while heap and query > heap[0][0]:
                val, i, j = heapq.heappop(heap)
                count += 1

                for di, dj in moves:
                    ni, nj = i + di, j + dj
                    if (
                        0 <= ni < m and
                        0 <= nj < n and
                        (ni, nj) not in visited
                    ):
                        heapq.heappush(heap, (grid[ni][nj], ni, nj))
                        visited.add((ni, nj))

            ans[idx] = count

        return ans