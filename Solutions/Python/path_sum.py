"""
    [EASY]
    112. Path Sum

    Concepts:
    - depth-first search
    - binary tree

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 17.82 MB  [Beats 9.88%]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], target: int) -> bool:
        
        def dfs(curr, path_sum):
            outcome = False

            if not curr.left and not curr.right and path_sum == target:
                return True

            if curr.left:
                outcome |= dfs(curr.left, path_sum + curr.left.val)
            if curr.right:
                outcome |= dfs(curr.right, path_sum + curr.right.val)

            return outcome

        return dfs(root, root.val) if root else False