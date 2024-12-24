"""
    [MEDIUM]
    2471. Minimum Number of Operations to Sort a Binary Tree by Level

    Concepts:
    - binary tree
    - breadth-first search

    Stats:
        Runtime | 143 ms    [Beats 67.86%]
        Memory  | 50.48 MB  [Beats 77.40%]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:

        def swapSort(A: list) -> int:
            count = 0
            vals = {val : i for i, val in enumerate(A)}
            sorted_A = sorted(A)

            for i in range(len(A)):
                if A[i] != sorted_A[i]:
                    # store index of value to be swapped
                    j = vals[sorted_A[i]]
                    # swap elements
                    A[i], A[j] = A[j], A[i]
                    # update elements' index
                    vals[A[i]] = i
                    vals[A[j]] = j

                    count += 1

            return count

        # bfs
        queue = deque([root])
        swap_count = 0

        while queue:
            len_q = len(queue)
            level = []

            for _ in range(len_q):
                curr = queue.popleft()
                level.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            swap_count += swapSort(level)

        return swap_count