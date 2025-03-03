"""
    [HARD]
    23. Merge k Sorted Lists

    Concepts:
    - heap/priority queue
    - linked list

    Stats:
        Runtime | 9 ms      [Beats 73.13%]
        Memory  | 21.20 MB  [Beats 6.06%]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
            Keep a priority queue with all heads of linked lists
            Pop off heap and push next value until no values left
        """
        dummy = ListNode()
        heap = []
        id_to_node = {}

        # append all head nodes to heap
        for head in lists:
            if head:
                id_to_node[id(head)] = head
                heap.append((head.val, id(head)))

        heapq.heapify(heap)

        head = dummy
        while heap:
            curr = id_to_node[heapq.heappop(heap)[1]]
            nxt = curr.next

            # keep heap size <= k
            del id_to_node[id(curr)]
            id_to_node[id(nxt)] = nxt

            # push next node to heap
            if nxt:
                heapq.heappush(heap, (nxt.val, id(nxt)))

            head.next = curr
            head = head.next

        return dummy.next