"""
    [MEDIUM]
    2685. Count the Number of Complete Components

    Concepts:
    - graph
    - depth-first search

    Stats:
        Runtime | 55 ms     [Beats 46.85%]
        Memory  | 18.89 MB  [Beats 5.93%]
"""

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        components = []
        graph = {i : set() for i in range(n)}
        visited = set()

        # build graph
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        def dfs(curr: int) -> None:
            nonlocal visited, components

            visited.add(curr)
            components[-1].append(curr)

            for node in graph[curr]:
                if node not in visited:
                    dfs(node)

        for node in graph:
            if node not in visited:
                # group connected components
                components.append([])
                dfs(node)
        
        for comp in components:
            # check if completely connected component group
            for node in comp:
                if len(graph[node]) != len(comp) - 1:
                    break
            else:
                count += 1

        return count