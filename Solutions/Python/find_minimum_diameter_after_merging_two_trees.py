"""
    [HARD]
    3203. Find Minimum Diameter After Merging Two Trees

    Concepts:
    - tree
    - breadth-first search

    Stats:
        Runtime | 498 ms    [Beats 62.42%]
        Memory  | 83.36 MB  [Beats 69.13%]
"""

class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        """
            1) Compute diameter of both trees
            2) From tree with biggest diameter, connect
                smaller tree to node half diameter into tree
            3) Return diameter of new tree
        """

        def getDiameter(edges: List[List[int]]) -> int:
            # adjacency list
            tree = defaultdict(list)
            for src, snk in edges:
                tree[src].append(snk)
                tree[snk].append(src)

            size = len(edges)

            # find furthest node
            q = deque([0])

            for _ in range(2):
                longest_path = 0
                visited = set()

                while q:
                    longest_path += 1
                    for _ in range(len(q)):
                        curr = q.popleft()
                        visited.add(curr)
                        for node in tree[curr]:
                            if node not in visited:
                                q.append(node)

                q = deque([curr])

            return longest_path - 1

        diam1 = getDiameter(edges1)
        diam2 = getDiameter(edges2)

        return max(diam1, diam2, ceil(diam1 / 2) + ceil(diam2 / 2) + 1)
