"""
    [HARD]
    25. Reverse Nodes in k-Group

    Concepts:
    - linked list
    - recursion

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 18.70 MB  [Beats 40.89%]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        idx = 0
        nodes = []
        curr = head

        # build group
        while curr and idx != k:
            nodes.append(curr)
            idx += 1
            curr = curr.next

        # do not reverse if < k nodes left
        if len(nodes) != k:
            return head

        # reverse nodes
        for i in range(1, k):
            nodes[i].next = nodes[i-1]
        
        # continue iteration
        nodes[0].next = self.reverseKGroup(curr, k)

        return nodes[-1]