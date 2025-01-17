"""
    [MEDIUM]
    114. Flatten Binary Tree to Linked List

    Concepts:
    - binary tree
    - linked list
    - depth-first search

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 17.82 MB  [Beats 47.36%]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prot = [] # pre-order traversal

        def dfs(curr: TreeNode):
            nonlocal prot
            
            if not curr:
                return

            prot.append(curr)
            dfs(curr.left)
            dfs(curr.right)

        dfs(root)

        for i in range(len(prot) - 1):
            prot[i].left = None
            prot[i].right = prot[i+1]