"""
    [MEDIUM]
    889. Construct Binary Tree from Preorder and Postorder Traversal

    Concepts:
    - binary tree
    - divide and conquer

    Stats:
        Runtime | 7 ms      [Beats 8.07%]
        Memory  | 17.93 MB  [Beats 27.16%]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(
        self, preorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:
    
        def construct(prot, pot) -> TreeNode:
            if not prot or not pot:
                return None

            root = TreeNode(prot[0])

            if len(prot) > 1 and prot[1] in pot:
                idx = pot.index(prot[1])
                root.left = construct(prot[1:1+idx+1], pot[:idx+1])
                root.right = construct(prot[1+idx+1:], pot[idx+1:])

            return root

        return construct(preorder, postorder)