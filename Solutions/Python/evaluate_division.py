"""
    [MEDIUM]
    399. Evaluate Division

    Concepts:
    - graph
    - depth-first search

    Stats:
        Runtime | 2 ms      [Beats 10.31%]
        Memory  | 17.94 MB  [Beats 48.64%]
"""

class Solution:
    def calcEquation(
        self,
        equations: List[List[str]],
        values: List[float],
        queries: List[List[str]]
    ) -> List[float]:

        res = [-1.0]*len(queries)
        # store nodes and their edge weights
        nodes = defaultdict(set)
        edges = defaultdict(set)

        for i, (num, denom) in enumerate(equations):
            # set edges to self
            nodes[num].add(num)
            nodes[denom].add(denom)
            edges[(num, num)] = 1.0 if num else 0.0
            edges[(denom, denom)] = 1.0 if denom else 0.0
            # set edges in both directions
            nodes[num].add(denom)
            nodes[denom].add(num)
            edges[(num, denom)] = values[i] if denom else float("inf")
            edges[(denom, num)] = 1.0 / values[i] if num else float("inf")

        def dfs(
            node: str,
            target: str,
            value: float,
            visited: set[str]
        ) -> float:

            nonlocal val

            if target in nodes[node]:
                val = value * edges[(node, target)]
                return True

            for n in nodes[node]:
                if (
                    n not in visited and
                    dfs(
                        n,
                        target,
                        value * edges[(node, n)],
                        visited | {node}
                    )
                ):
                    return True

            return False

        for i, (num, denom) in enumerate(queries):
            val = None
            dfs(num, denom, 1.0, set())
            if val is not None:
                res[i] = val

        return res