"""
    [MEDIUM]
    3243. Shortest Distance After Road Addition Queries I

    Concepts:
    - graph
    - breadth-first search

    Stats:
        Runtime | 549 ms    [Beats 62.78%]
        Memory  | 17.91 MB  [Beats 8.31%]
"""

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        """
            cities in range(n) are a digraph in top sort

            return array of shortest path from city 0 to
            city n-1 after each query update

            perform bfs after updating each query
        """
        res = [float("inf")]*len(queries)

        # stores destinations from each city
        road = {i : [i+1] for i in range(n-1)} | {n-1 : []}


        def bfs():
            nonlocal road

            queue = deque([(0, 0)])
            visited = set()

            while queue:
                len_q = len(queue)

                for _ in range(len_q):
                    curr, dist = queue.popleft()

                    if curr == n - 1:
                        return dist

                    for child in road[curr]:
                        if child not in visited:
                            queue.append((child, dist + 1))
                            visited.add(child)
            
            return 0


        # run bfs following each query update
        for i, query in enumerate(queries):
            src, snk = query
            road[src].append(snk)

            res[i] = bfs()

        return res