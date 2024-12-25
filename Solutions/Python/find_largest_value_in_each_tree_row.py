"""
    [MEDIUM]
    515. Find Largest Value in Each Tree Row

    Concepts:
    - binary tree
    - breadth-first search

    Stats:
        Runtime | 3 ms      [Beats 48.85%]
        Memory  | 19.94 MB  [Beats 6.38%]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        def bfs(root):
            if not root:
                return []

            queue = deque([root])
            levels = []

            while queue:
                len_q = len(queue)
                level_max = -float("inf")

                for _ in range(len_q):
                    curr = queue.popleft()
                    level_max = max(curr.val, level_max)

                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
                    
                levels.append(level_max)

            return levels

        return bfs(root)