"""
    [MEDIUM]
    117. Populating Next Right Pointers in Each Node II

    Concepts:
    - binary tree
    - breadth-first search

    Stats:
        Runtime | 35 ms     [Beats 96.16%]
        Memory  | 18.98 MB  [Beats 18.71%]
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """
            Level-Order Traversal with extra steps
        """
        if not root:
            return None

        queue = deque([root])
        level = []

        while queue:
            len_q = len(queue)

            if level:
                for i in range(len_q - 1):
                    level[i].next = level[i+1]
                level.clear()

            for _ in range(len_q):
                curr = queue.popleft()

                if curr.left:
                    queue.append(curr.left)
                    level.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                    level.append(curr.right)

        return root