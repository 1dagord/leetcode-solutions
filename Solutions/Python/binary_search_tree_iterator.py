"""
    [MEDIUM]
    173. Binary Search Tree Iterator

    Concepts:
    - binary search tree
    - depth-first search

    Stats:
        Runtime | 5 ms      [Beats 72.25%]
        Memory  | 25.01 MB  [Beats 26.69%]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.curr = -1
        self.iot = []

        def dfs(curr):
            if not curr:
                return

            dfs(curr.left)
            self.iot.append(curr.val)
            dfs(curr.right)

        dfs(root)
        self.n = len(self.iot)
        

    def next(self) -> int:
        self.curr += 1
        return self.iot[self.curr]

    def hasNext(self) -> bool:
        if self.curr == -1:
            return self.iot[0] is not None

        return self.curr + 1 < self.n

        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()