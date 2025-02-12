"""
    [MEDIUM]
    129. Sum Root to Leaf Numbers

    Concepts:
    - binary tree
    - depth-first search

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 17.85 MB  [Beats 33.79%]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        rtl_sum = 0
        convert = lambda l: sum(v * (10 ** i) for i, v in enumerate(l[::-1]))

        def dfs(curr: TreeNode, path: list[int]):
            nonlocal rtl_sum

            if curr.left:
                dfs(curr.left, path + [curr.left.val])
            if curr.right:
                dfs(curr.right, path + [curr.right.val])

            if not curr.left and not curr.right:
                rtl_sum += convert(path)

        dfs(root, [root.val])

        return rtl_sum