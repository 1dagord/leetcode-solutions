"""
    [HARD]
    2127. Maximum Employees to Be Invited to a Meeting

    Concepts:
    - graph
    - breadth-first search

    Stats:
        Runtime | 315 ms    [Beats 43.75%]
        Memory  | 53.08 MB  [Beats 44.71%]
"""

from collections import deque, defaultdict

class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        """
            Attendees will be members of largest cycle in graph
            Graph may have disjoint components

            Cycles can either be open or closed
                closed: one big loop; last node points
                        back to the first
                open: two or more nodes point to each other

            1) build graph with all nodes
            2) iterate over all nodes and store length
                of longest cycle
            3) for employees without two connections,
                append outer employees with connections
                to employees in longest cycle
        """
        # 1) Find longest cycle
        n = len(favorite)
        longest = 0             # length of longest cycle
        seen = [False]*n        # nodes traversed in EVERY traversal
        length_2_cycles = []    # cycles of length 2

        # start traversal from every person
        for person in range(n):
            if not seen[person]:
                start, curr = person, person

                # nodes traversed in CURRENT traversal
                curr_trav = set()

                while not seen[curr]:
                    seen[curr] = True
                    curr_trav.add(curr)

                    # update current person
                    curr = favorite[curr]

                if curr in curr_trav:
                    length = len(curr_trav)

                    while start != curr:
                        length -= 1
                        start = favorite[start]

                    longest = max(longest, length)

                    if length == 2:
                        length_2_cycles.append([curr, favorite[curr]])


        # 2) Find sum of longest open cycles
        inverted = defaultdict(list)

        for snk, src in enumerate(favorite):
            inverted[src].append(snk)

        def bfs(src: int, parent: int) -> int:
            queue = deque([(src, 0)]) # node, length
            max_length = 0

            while queue:
                node, length = queue.popleft()

                if node == parent:
                    continue

                max_length = max(length, max_length)
                for nei in inverted[node]:
                    queue.append((nei, length + 1))

            return max_length

        # sum of chained open cycles
        chain_sum = 0
        for n1, n2 in length_2_cycles:
            chain_sum += bfs(n1, n2) + bfs(n2, n1) + 2

        return max(chain_sum, longest)
