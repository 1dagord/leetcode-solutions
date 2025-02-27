"""
    [MEDIUM]
    207. Course Schedule

    Concepts:
    - depth-first search
    - graph
    - topological sort

    Stats:
        Runtime | 7 ms      [Beats 49.42%]
        Memory  | 19.33 MB  [Beats 42.73%]
"""

class Solution:
    def canFinish(self, num_courses: int, prereqs: List[List[int]]) -> bool:
        graph = defaultdict(list)
        taken = {}

        for c, p in prereqs:
            graph[c].append(p)

        def dfs(course: int) -> bool:
            nonlocal taken

            # if cycle detected...
            if course in taken:
                return taken[course]

            # assume cannot be taken until all
            # prerequisites are taken
            taken[course] = False

            for pre in graph[course]:
                # if any prereqs cannot be completed,
                # current course cannot be completed
                if not dfs(pre):
                    return taken[course]
            
            taken[course] = True

            return taken[course]

        for course in range(num_courses):
            if not dfs(course):
                return False

        return True