"""
    [MEDIUM]
    106. Construct Binary Tree from Inorder and Postorder Traversal

    Concepts:
    - binary tree
    - divide and conquer

    Stats:
        Runtime | 88 ms     [Beats 35.44%]
        Memory  | 89.44 MB  [Beats 21.10%]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def construct(iot, pot):
            if not iot or not pot:
                return None

            root = TreeNode(pot[-1])

            # index of root in pot
            idx = iot.index(pot[-1])
            
            # iot: pass left subarray excluding current value
            # pot: pass nodes before and including next root
            root.left = construct(iot[:idx], pot[:idx])
            # iot: pass right subarray excluding current value
            # pot: pass node between left root and current root; exclusive
            root.right = construct(iot[idx + 1:], pot[idx : -1])

            return root

        return construct(inorder, postorder)