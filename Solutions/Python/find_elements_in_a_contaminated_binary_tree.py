"""
    [MEDIUM]
    1261. Find Elements in a Contaminated Binary Tree

    Concepts:
    - binary tree
    - hash table
    - design

    Stats:
        Runtime | 5 ms      [Beats 73.52%]
        Memory  | 22.16 MB  [Beats 73.39%]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.root.val = 0
        self.values = set()

        def recover(curr: TreeNode) -> int:
            if not curr:
                return

            self.values.add(curr.val)

            if curr.left:
                curr.left.val = 2 * curr.val + 1
                recover(curr.left)
            if curr.right:
                curr.right.val = 2 * curr.val + 2
                recover(curr.right)

        recover(self.root)

    def find(self, target: int) -> bool:
        return target in self.values

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)