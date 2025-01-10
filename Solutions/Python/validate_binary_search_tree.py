"""
    [MEDIUM]
    98. Validate Binary Search Tree

    Concepts:
    - binary search tree
    - depth-first search

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 19.52 MB  [Beats 38.52%]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        iot = []

        def dfs(curr):
            nonlocal iot

            if not curr:
                return

            if curr.left:
                dfs(curr.left)

            iot.append(curr.val)

            if curr.right:
                dfs(curr.right)

        dfs(root)
        
        for i in range(1, len(iot)):
            if iot[i-1] >= iot[i]:
                return False

        return True