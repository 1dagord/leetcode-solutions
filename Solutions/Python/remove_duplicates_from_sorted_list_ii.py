"""
    [MEDIUM]
    82. Remove Duplicates from Sorted List II

    Concepts:
    - linked list

    Stats:
        Runtime | 1 ms      [Beats 40.68%]
        Memory  | 18.09 MB  [Beats 12.89%]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        curr = head

        while curr:
            nodes.append(curr.val)
            curr = curr.next

        dummy = ListNode(-1)
        new_head = dummy
        for val in [k for k, v in Counter(nodes).items() if v == 1]:
            new_head.next = ListNode(val)
            new_head = new_head.next
        
        return dummy.next
