"""
    [EASY]
    101. Symmetric Tree

    Concepts:
    - binary tree
    - breadth-first search

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 16.55 MB  [Beats 100%]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
            Search both subtrees using BFS
            Compare each level to see if reverse of each other
        """

        def bfs(root):
            queue = deque([root])
            levels = []

            while queue:
                n = len(queue)
                level = []
                for _ in range(n):
                    curr = queue.popleft()
                    if curr:
                        level.append(curr.val)
                        queue.append(curr.left)
                        queue.append(curr.right)
                    else:
                        level.append(None)

                levels.append(level)

            return levels

        for level in bfs(root):
            if level != level[::-1]:
                return False

        return True