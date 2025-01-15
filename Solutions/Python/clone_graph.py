"""
    [MEDIUM]
    133. Clone Graph

    Concepts:
    - graph
    - breadth-first search

    Stats:
        Runtime | 42 ms     [Beats 55.70%]
        Memory  | 18.40 MB  [Beats 7.44%]
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import defaultdict, deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None or not node.neighbors:
            return None if node is None else Node(val=node.val)

        adj = defaultdict(set)  # int |-> set[int]

        # explore graph and update adjacency list
        queue = deque([node])
        while queue:
            len_q = len(queue)

            for _ in range(len_q):
                curr = queue.popleft()

                for n in curr.neighbors:
                    # if neighbor not explored...
                    if not adj[n]:
                        queue.append(n)
                        
                    adj[curr].add(n)

        # rebuild graph from adjacency list
        nodes = {n.val : Node(val=n.val) for n in adj}

        for nde, nei in adj.items():
            for nbr in nei:
                nodes[nde.val].neighbors.append(nodes[nbr.val])

        return nodes[node.val]