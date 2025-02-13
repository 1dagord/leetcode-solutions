"""
    [EASY]
    141. Linked List Cycle

    Concepts:
    - two pointers
    - linked list

    Stats:
        Runtime | 45 ms     [Beats 76.07%]
        Memory  | 19.71 MB  [Beats 83.64%]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tortoise = head
        hare = head

        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next

            if tortoise == hare:
                return True

        return False