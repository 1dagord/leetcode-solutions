"""
    [MEDIUM]
    138. Copy List with Random Pointer

    Concepts:
    - linked list
    - hash table

    Stats:
        Runtime | 36 ms     [Beats 70.78%]
        Memory  | 17.41 MB  [Beats 62.71%]
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        orig_to_cpy = {} # Node_Object -> node.val

        # associate each node object with a
        # new node of same value
        curr = head
        while curr:
            orig_to_cpy[curr] = Node(curr.val)
            curr = curr.next

        # link all new nodes together using
        # `next` and `random` of old nodes
        curr = head
        while curr:
            # .get() : returns value with given key or None if not in dict
            orig_to_cpy[curr].next = orig_to_cpy.get(curr.next)
            orig_to_cpy[curr].random = orig_to_cpy.get(curr.random)
            curr = curr.next

        # return copy of new list
        return orig_to_cpy[head]