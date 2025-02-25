"""
    [EASY]
    637. Average of Levels in Binary Tree

    Concepts:
    - binary tree
    - breadth-first search

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 19.87 MB  [Beats 81.73%]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        averages = []

        queue = deque([root])
        while queue:
            level_len = len(queue)
            level_sum = 0

            for _ in range(level_len):
                curr = queue.popleft()

                level_sum += curr.val

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            averages.append(level_sum / level_len)

        return averages