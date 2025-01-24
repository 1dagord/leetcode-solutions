"""
    [MEDIUM]
    802. Find Eventual Safe States

    Concepts:
    - graph
    - depth-first search
    - topological sort

    Stats:
        Runtime | 31 ms     [Beats 83.02%]
        Memory  | 23.91 MB  [Beats 24.29%]
"""

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = {}
        
        def dfs(idx: int) -> bool:
            nonlocal safe

            # if cycle detected...
            if idx in safe:
                return safe[idx]

            # assume not safe until after iteration
            safe[idx] = False

            for node in graph[idx]:
                # if any adjacent node not safe,
                # current node not safe
                if not dfs(node):
                    return safe[idx]

            safe[idx] = True

            return safe[idx]

        return [i for i in range(n) if dfs(i)]