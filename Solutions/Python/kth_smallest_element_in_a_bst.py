"""
    [MEDIUM]
    230. Kth Smallest Element in a BST

    Concepts:
    - binary search tree
    - depth-first search

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 21.15 MB  [Beats 7.70%]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
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
        return iot[k - 1]