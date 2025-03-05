"""
    [MEDIUM]
    210. Course Schedule II

    Concepts:
    - graph
    - topological sort
    - breadth-first search

    Stats:
        Runtime | 3 ms      [Beats 77.80%]
        Memory  | 19.09 MB  [Beats 73.83%]
"""

class Solution:
    def findOrder(self, n: int, prereqs: List[List[int]]) -> List[int]:
        """
            Kahn's Algorithm

            https://en.wikipedia.org/wiki/Topological_sorting
        """
        adj = defaultdict(list)
        indegree = [0]*n
        res = []

        for c, p in prereqs:
            # prereq -> course
            adj[p].append(c)
            indegree[c] += 1

        queue = deque([])
        for i in range(n):
            # if no prereqs...
            if indegree[i] == 0:
                queue.append(i)

        # contains courses w/ no prereqs
        while queue:
            curr = queue.popleft()
            res.append(curr)

            for next_course in adj[curr]:
                indegree[next_course] -= 1

                # if no more prereqs to be completed...
                if indegree[next_course] == 0:
                    queue.append(next_course)

        # cycle detection
        if any(indegree):
            return []

        # trivial solution: no prereqs
        return res