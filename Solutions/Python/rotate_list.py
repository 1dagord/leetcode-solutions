"""
    [MEDIUM]
    61. Rotate List

    Concepts:
    - linked list
    - two pointers

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 16.71 MB  [Beats 100%]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
            1) iterate into list until k == 0 or
                curr.next == None
            2) store new_head.next and set new_head.next = None
            3) set curr.next = head
            4) return new_head
        """
        if not head or not head.next:
            return head

        # mod k by length to avoid unnecessary work
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        k %= length

        # get new head
        curr = head
        while k:
            if not curr:
                curr = head
            curr = curr.next
            k -= 1

        # if at end of list, rotation is identical to list
        if not curr:
            return head
        
        new_head = head

        # iterate to end of array
        while curr.next:
            curr = curr.next
            new_head = new_head.next

        if new_head != curr:
            # store head value of rotated list
            next_head = new_head.next
            # set prev value's next to None
            new_head.next = None
            # point last node back to first
            curr.next = head
        else:
            next_head = head

        return next_head