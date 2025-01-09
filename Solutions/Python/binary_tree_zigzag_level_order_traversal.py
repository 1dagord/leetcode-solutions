"""
    [MEDIUM]
    103. Binary Tree Zigzag Level Order Traversal

    Concepts:
    - binary tree
    - breadth-first search

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 17.94 MB  [Beats 26.58%]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # level order, but reverse every other level
        levels = []
        direction = 1

        if not root:
            return []

        queue = deque([root])
        while queue:
            n = len(queue)
            level = []

            for _ in range(n):
                curr = queue.popleft()
                level.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            levels.append(level[::direction])
            direction *= -1

        return levels