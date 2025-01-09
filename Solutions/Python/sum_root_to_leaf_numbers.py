"""
    [MEDIUM]
    129. Sum Root to Leaf Numbers

    Concepts:
    - binary tree
    - depth-first search

    Stats:
        Runtime | 1 ms      [Beats 9.28%]
        Memory  | 17.77 MB  [Beats 16.97%]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        nums = []

        if not root:
            return 0
        
        def dfs(curr: TreeNode, path: str):
            nonlocal nums

            if not curr.left and not curr.right:
                nums.append(path)

            if curr.left:
                dfs(curr.left, path + str(curr.left.val))
            if curr.right:
                dfs(curr.right, path + str(curr.right.val))


        dfs(root, str(root.val))
        return sum([int(num) for num in nums])