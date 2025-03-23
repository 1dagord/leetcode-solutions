"""
    [MEDIUM]
    1976. Number of Ways to Arrive at Destination

    Concepts:
    - graph
    - shortest path
    - dynamic programming

    Stats:
        Runtime | 21 ms     [Beats 48.54%]
        Memory  | 24.96 MB  [Beats 86.77%]
"""

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        """
            Dijkstra

            Typical Dijkstra, but keep track of 
            number of ways to get to each node

            Update number of ways if current distance ==
            minimum distance at each node
        """
        vertices = defaultdict(list)

        for u, v, time in roads:
            vertices[u].append((v, time))
            vertices[v].append((u, time))

        distances = {v : float("inf") for v in vertices}
        distances[0] = 0

        ways = [0]*n
        ways[0] = 1     # 1 way to get to self

        pq = [(0, 0)]   # distance, node
        visited = set()

        while pq:
            curr_dist, curr_node = heapq.heappop(pq)

            if curr_node in visited:
                continue
            visited.add(curr_node)

            for nei, dist in vertices[curr_node]:
                new_dist = curr_dist + dist

                # if shorter distance found...
                if new_dist < distances[nei]:
                    # ...update distance and number of ways
                    distances[nei] = new_dist
                    ways[nei] = ways[curr_node]
                    heapq.heappush(pq, (new_dist, nei))

                # if same distance as minimum...
                elif new_dist == distances[nei]:
                    # ...increment number of ways
                    ways[nei] += ways[curr_node]

        return ways[n-1] % ((10 ** 9) + 7)