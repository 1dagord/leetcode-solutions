"""
    [MEDIUM]
    427. Construct Quad Tree

    Concepts:
    - matrix
    - divide and conquer

    Stats:
        Runtime | 92 ms     [Beats 69.54%]
        Memory  | 18.58 MB  [Beats 54.99%]
"""

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        counts = [0, 0]

        for i in range(n):
            for j in range(n):
                counts[grid[i][j]] += 1

                if counts[0] and counts[1]:
                    return Node(
                        val=1
                        , isLeaf=False
                        , topLeft=self.construct(
                            [row[:n//2] for row in grid[:n//2]]
                        )
                        , topRight=self.construct(
                            [row[n//2:] for row in grid[:n//2]]
                        )
                        , bottomLeft=self.construct(
                            [row[:n//2] for row in grid[n//2:]]
                        )
                        , bottomRight=self.construct(
                            [row[n//2:] for row in grid[n//2:]]
                        )
                    ) 
                    
        return Node(
            val=grid[0][0]
            , isLeaf=True
            , topLeft=None
            , topRight=None
            , bottomLeft=None
            , bottomRight=None
        )