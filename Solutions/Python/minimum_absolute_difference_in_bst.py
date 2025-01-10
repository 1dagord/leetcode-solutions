"""
    [MEDIUM]
    530. Minimum Absolute Difference in BST

    Concepts:
    - binary search tree
    - depth-first search

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 18.76 MB  [Beats 86.29%]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        iot = []    # in-order traversal
        min_diff = float("inf")

        def dfs(curr):
            nonlocal iot

            if curr.left:
                dfs(curr.left)

            iot.append(curr.val)

            if curr.right:
                dfs(curr.right)

        dfs(root)
        
        for i in range(1, len(iot)):
            min_diff = min(min_diff, iot[i] - iot[i-1])

        return min_diff