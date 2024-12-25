"""
    [EASY]
    222. Count Complete Tree Nodes

    Concepts:
    - binary tree
    - depth-first search

    Stats:
        Runtime | 7 ms      [Beats 23.47%]
        Memory  | 23.33 MB  [Beats 10.13%]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        count = 0
        
        def dfs(curr):
            nonlocal count
            if not curr:
                return

            count += 1
            dfs(curr.left)
            dfs(curr.right)

        dfs(root)
        return count