"""
    [HARD]
    124. Binary Tree Maximum Path Sum

    Concepts:
    - binary tree
    - depth-first search

    Stats:
        Runtime | 14 ms     [Beats 68.66%]
        Memory  | 22.92 MB  [Beats 59.94%]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_sum = -float("inf")

        def traverse(curr: TreeNode) -> int:
            nonlocal max_path_sum

            if not curr:
                return 0

            left = max(0, traverse(curr.left))
            right = max(0, traverse(curr.right))

            # compare with path made from subtrees
            max_path_sum = max(
                max_path_sum,
                left + right + curr.val
            )

            # return max of subtrees and current value
            # returns only current value at leaf
            return max(left, right) + curr.val

        traverse(root)

        return max_path_sum
            