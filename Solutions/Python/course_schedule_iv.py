"""
    [MEDIUM]
    1462. Course Schedule IV

    Concepts:
    - topological sort
    - depth-first search

    Stats:
        Runtime | 234 ms    [Beats 34.52%]
        Memory  | 26.75 MB  [Beats 5.01%]
"""

from functools import cache

class Solution:
    def checkIfPrerequisite(
            self,
            num_courses: int,
            prereqs: List[List[int]],
            queries: List[List[int]]
        ) -> List[bool]:

        ans = [False]*len(queries)
        outgoing = defaultdict(set)

        # construct graph
        for a, b in prereqs:
            outgoing[a].add(b)

        @cache
        def dfs(curr: int, target: int) -> bool:
            # returns true if b is prereq of a
            outcome = False

            if curr not in outgoing:
                return False

            if target in outgoing[curr]:
                return True

            for node in outgoing[curr]:
                outcome |= dfs(node, target)

            return outcome
            

        for i, (a, b) in enumerate(queries):
            # run dfs
            ans[i] = dfs(a, b)

        return ans