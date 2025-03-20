"""
    [HARD]
    3108. Minimum Cost Walk in Weighted Graph

    Concepts:
    - union find
    - bit manipulation

    Stats:
        Runtime | 131 ms    [Beats 99.28%]
        Memory  | 94.26 MB  [Beats 31.88%]
"""

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        parent = list(range(n))
        rank = [1]*n
        weight = [-1]*n
        
        def find(x: int) -> int:
            # if x is not representative...
            if parent[x] != x:
                # ...keep searching
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x: int, y: int, w: int) -> None:
            xrep = find(x)
            yrep = find(y)

            # if x and y in same set...
            if xrep == yrep:
                weight[xrep] &= w
                return
            
            if rank[xrep] > rank[yrep]:
                parent[yrep] = xrep
                rank[xrep] += rank[yrep]
                weight[xrep] &= weight[yrep] & w
            else:
                parent[xrep] = yrep
                rank[yrep] += rank[xrep]
                weight[yrep] &= weight[xrep] & w


        ans = []

        # union all disjoint sets
        for u, v, w in edges:
            union(u, v, w)

        # if in same set, append weight
        for u, v in query:
            pu, pv = find(u), find(v)
            ans.append(
                weight[pu]
                if pu == pv
                else -1
            )

        return ans