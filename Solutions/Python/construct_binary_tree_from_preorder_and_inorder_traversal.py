"""
    [MEDIUM]
    105. Construct Binary Tree from Preorder and Inorder Traversal

    Concepts:
    - binary tree
    - divide and conquer

    Stats:
        Runtime | 92 ms     [Beats 47.80%]
        Memory  | 89.35 MB  [Beats 20.32%]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def construct(prot, iot) -> TreeNode:
            if not prot or not iot:
                return None

            root = TreeNode(prot[0])

            # index of root in iot
            idx = iot.index(prot[0])

            # prot: pass only node following root
            # iot: pass left subarray excluding current value
            root.left = construct(prot[1:idx + 1], iot[:idx])
            # prot: pass all nodes following root
            # iot: pass right subarray excluding current value
            root.right = construct(prot[idx + 1:], iot[idx + 1:])

            return root

        return construct(preorder, inorder)