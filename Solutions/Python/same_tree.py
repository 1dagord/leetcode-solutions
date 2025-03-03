"""
    [EASY]
    100. Same Tree

    Concepts:
    - binary tree
    - breadth-first search

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 16.70 MB  [Beats 100%]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def bfs(root1, root2):
            queue1 = deque([root1])
            queue2 = deque([root2])

            while queue1 and queue2:
                n1 = len(queue1)
                n2 = len(queue2)
                
                if n1 != n2:
                    return False

                for _ in range(n1):
                    curr1 = queue1.popleft()
                    curr2 = queue2.popleft()

                    if (curr1 and not curr2) or (curr2 and not curr1):
                        return False
                    if curr1 and curr2:
                        if curr1.val != curr2.val:
                            return False

                    for curr, queue in [(curr1, queue1), (curr2, queue2)]:
                        if curr:
                            queue.append(curr.left)
                            queue.append(curr.right)
                
            return True

        return bfs(p, q)