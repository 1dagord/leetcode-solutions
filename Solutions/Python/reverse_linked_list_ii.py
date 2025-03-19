"""
    [MEDIUM]
    92. Reverse Linked List II

    Concepts:
    - linked list

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 16.70 MB  [Beats 100%]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
            Use LIFO properties of stack to reverse node
            and splice together reversed portion with
            prepended and appended list
        """
        dummy = ListNode(0, head)
        pre = dummy
        prev = dummy
        curr = dummy
        post = head

        res = dummy

        if left == right:
            return head

        # shift in curr and post pointers
        while (right - left):
            curr = curr.next
            post = post.next
            right -= 1
        
        while left:
            if left > 1:
                pre = pre.next

            prev = prev.next
            curr = curr.next
            post = post.next

            left -= 1

        # add nodes to stack
        middle_nodes = []

        # get all nodes in between
        temp = prev
        while temp != post:
            middle_nodes.append(temp)
            temp = temp.next

        # pop nodes off stack and append to list
        while middle_nodes:
            node = middle_nodes.pop()
            pre.next = node
            pre = pre.next


        if post:
            pre.next = post
        else:
            pre.next = None

        return res.next