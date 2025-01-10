"""
    [EASY]
    226. Invert Binary Tree

    Concepts:
    - binary tree
    - breadth-first search

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 17.61 MB  [Beats 31.70%]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        queue = deque([root])
        while queue:
            n = len(queue)

            for _ in range(n):
                node = queue.popleft()

                node.left, node.right = node.right, node.left

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root