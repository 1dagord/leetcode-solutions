"""
    [MEDIUM]
    199. Binary Tree Right Side View

    Concepts:
    - binary tree
    - breadth-first search

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 17.88 MB  [Beats 12.84%]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # level order, but only keep last element
        levels = []

        if not root:
            return []

        queue = deque([root])
        while queue:
            n = len(queue)

            for i in range(n):
                curr = queue.popleft()

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

                if i == n - 1:
                    levels.append(curr.val)

        return levels