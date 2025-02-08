"""
    [MEDIUM]
    148. Sort List

    Concepts:
    - linked list
    - sorting

    Stats:
        Runtime | 26 ms     [Beats 89.96%]
        Memory  | 33.01 MB  [Beats 19.91%]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        curr = head

        while curr:
            nodes.append(curr)
            curr = curr.next

        for node in nodes:
            node.next = None

        n = len(nodes)

        # implements timsort under the hood
        nodes.sort(key=lambda x: x.val)
        nodes += [None]

        for i in range(n):
            nodes[i].next = nodes[i+1]

        return nodes[0]