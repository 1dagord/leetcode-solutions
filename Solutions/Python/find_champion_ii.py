"""
    [MEDIUM]
    2924. Find Champion II

    Concepts:
    - graph

    Stats:
        Runtime | 20 ms     [Beats 19.87%]
        Memory  | 18.32 MB  [Beats 9.65%]
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.incoming = []
        self.outgoing = []

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        """
            Directed Acyclic Graph
            Edge points from strongest to weakest team

            Return node with no incoming edges if unique
            Else, return -1
        """
        if not edges:
            return 0 if n <= 1 else -1

        # if too few edges...
        if len(edges) < n - 1:
            return -1

        nodes = {} # int -> Node
        for src, snk in edges:

            # check for membership
            if src not in nodes:
                # create new node
                src_node = Node(src)
                nodes[src] = src_node
            else:
                src_node = nodes[src]

            if snk not in nodes:
                # create new node
                snk_node = Node(snk)
                nodes[snk] = snk_node
            else:
                snk_node = nodes[snk]

            src_node.outgoing.append(snk)
            snk_node.incoming.append(src)

        # if not all nodes reachable...
        if len(nodes) != n:
            return -1

        # find unique node w no incoming
        # else, return -1
        strongest = None
        for node in list(nodes.values()):
            if not node.incoming:
                if strongest:
                    return -1
                strongest = node

        return strongest.val