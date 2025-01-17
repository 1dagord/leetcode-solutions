"""
    [MEDIUM]
    117. Populating Next Right Pointers in Each Node II

    Concepts:
    - binary tree
    - breadth-first search

    Stats:
        Runtime | 53 ms     [Beats 10.12%]
        Memory  | 18.92 MB  [Beats 18.71%]
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

        while queue:
            len_q = len(queue)
            level = queue.copy()

            for _ in range(len_q):
                curr = queue.popleft()

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            for i in range(len_q - 1):
                level[i].next = level[i+1]

        return root