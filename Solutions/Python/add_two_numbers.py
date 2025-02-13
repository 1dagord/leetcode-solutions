"""
    [MEDIUM]
    2. Add Two Numbers

    Concepts:
    - linked list
    - math

    Stats:
        Runtime | 1 ms      [Beats 82.59%]
        Memory  | 18.09 MB  [Beats 14.09%]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        res = ListNode(-1, -1)
        head = res

        while l1 and l2:
            num = l1.val + l2.val + carry
            carry = 1 if num > 9 else 0

            res.next = ListNode(num % 10)
            res = res.next

            l1 = l1.next
            l2 = l2.next

        while l1:
            num = l1.val + carry
            carry = 1 if num > 9 else 0

            res.next = ListNode(num % 10)
            res = res.next

            l1 = l1.next

        while l2:
            num = l2.val + carry
            carry = 1 if num > 9 else 0

            res.next = ListNode(num % 10)
            res = res.next
            
            l2 = l2.next

        res.next = ListNode(1) if carry else None

        return head.next