"""
    [MEDIUM]
    684. Redundant Connection

    Concepts:
    - graph
    - union find

    Stats:
        Runtime | 2 ms      [Beats 64.41%]
        Memory  | 18.12 MB  [Beats 61.58%]
"""

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
            Union Find

            When two nodes have same representative,
            the cycle has beenn found
        """
        n = len(edges)
        parent = [i for i in range(n + 1)]
        rank = [1]*(n + 1)

        def find(node: int) -> int:
            """
                Traverse set until representative found
            """
            if node != parent[node]:
                parent[node] = find(parent[node])
            return parent[node]

        def union(node1: int, node2: int) -> bool:
            """
                Returns True if nodes are not a part
                of same set, False otherwise
            """
            p1, p2 = find(node1), find(node2)

            # if same representative, nodes already
            # belong to same set
            if p1 == p2:
                return False

            # union disjoint sets
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]

            return True

        for src, snk in edges:
            if not union(src, snk):
                return [src, snk]