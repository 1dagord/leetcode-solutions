"""
    [MEDIUM]
    236. Lowest Common Ancestor of a Binary Tree

    Concepts:
    - binary tree
    - depth-first search

    Stats:
        Runtime | 51 ms     [Beats 65.14%]
        Memory  | 22.00 MB  [Beats 42.82%]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # leaf reached or empty tree
        if not root:
            return

        # if p or q found...
        if root in [p, q]:
            return root

        # recursively search left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # if a target found in both, return current node
        if left and right:
            return root

        # if only found in one subtree, return root of subtree
        return left if left else right