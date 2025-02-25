"""
    [MEDIUM]
    148. Sort List

    Concepts:
    - linked list
    - sorting

    Stats:
        Runtime | 183 ms    [Beats 56.91%]
        Memory  | 32.92 MB  [Beats 41.86%]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def findMiddle(head: ListNode):
            slow = head
            fast = head.next

            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            
            return slow

        def merge(left: ListNode, right: ListNode):
            l = left
            r = right
            dummy = ListNode(-1)
            curr = dummy

            while l and r:
                if l.val < r.val:
                    curr.next = l
                    curr = l
                    l = l.next
                else:
                    curr.next = r
                    curr = r
                    r = r.next
                
            curr.next = l if l else r

            return dummy.next

        def mergeSort(head: ListNode):
            if not head or not head.next:
                return head

            middle = findMiddle(head)
            left_head = head
            right_head = middle.next
            middle.next = None

            left = mergeSort(left_head)
            right = mergeSort(right_head)

            return merge(left, right)
        
        return mergeSort(head)