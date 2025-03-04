"""
    [MEDIUM]
    86. Partition List

    Concepts:
    - linked list

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 17.68 MB  [Beats 91.52%]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lt = ListNode(-1)
        gte = ListNode(-1)
        lt_head = lt
        gte_head = gte

        curr = head

        while curr:
            if curr.val < x:
                lt.next = curr
                lt = lt.next
            else:
                gte.next = curr
                gte = gte.next

            curr = curr.next

        lt.next = gte_head.next
        gte.next = None

        return lt_head.next