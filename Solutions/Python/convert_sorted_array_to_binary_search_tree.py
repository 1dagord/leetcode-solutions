"""
    [MEDIUM]
    108. Convert Sorted Array to Binary Search Tree

    Concepts:
    - binary search tree
    - divide & conquer

    Stats:
        Runtime | 3 ms      [Beats 73.42%]
        Memory  | 17.92 MB  [Beats 81.97%]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # recursively find middle element
        def createSubtree(arr):
            # create subtree based on values left and right
            # of middle index of arr
            n = len(arr)
            mid_ind = n // 2

            if n == 0:
                return None

            curr = TreeNode(arr[mid_ind])
            curr.left = createSubtree(arr[:mid_ind])
            curr.right = createSubtree(arr[mid_ind+1:])

            return curr

        return createSubtree(nums)