"""
    [MEDIUM]
    19. Remove Nth Node From End of List

    Concepts:
    - linked list
    - two pointers

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 16.58 MB  [Beats 96.14%]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head

        # iterate n nodes into list
        while n:
            curr = curr.next
            n -= 1

        # prepend dummy node so prev.next is node to delete
        dummy = ListNode(None, head)
        prev = dummy

        # put prev into position
        while curr:
            prev = prev.next
            curr = curr.next

        # if already at end of list, remove first element
        if prev == dummy:
            return head.next

        # splice out node
        prev.next = prev.next.next

        return head