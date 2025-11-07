"""
    [MEDIUM]
    3217. Delete Nodes From Linked List Present in Array

    Concepts:
    - linked list
    - hash table

    Stats:
        Runtime | 56 ms     [Beats 67.02%]
        Memory  | 58.48 MB  [Beats 77.39%]
"""

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        dummy = ListNode(-1, head)
        prev, curr = dummy, dummy.next

        while curr:
            while curr and curr.val in nums:
                curr = curr.next
                prev.next = curr

            if not curr:
                break

            prev = curr
            curr = curr.next

        return dummy.next