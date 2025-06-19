"""
    [MEDIUM]
    236. Lowest Common Ancestor of a Binary Tree

    Concepts:
    - binary tree
    - depth-first search

    Stats:
        Runtime | 57 ms     [Beats 34.88%]
        Memory  | 21.80 MB  [Beats 91.80%]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lca(curr: TreeNode) -> TreeNode:
            if not curr:
                return None
            
            if curr in [p, q]:
                return curr
            
            left = lca(curr.left)
            right = lca(curr.right)
            
            # if a target found in both, return current node
            if left and right:
                return curr
            
            # if only found in one subtree, return root of subtree
            return left if left else right
        
        return lca(root)
