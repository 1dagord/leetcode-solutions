"""
    [MEDIUM]
    433. Minimum Genetic Mutation

    Concepts:
    - string
    - breadth-first search

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 17.96 MB  [Beats 19.13%]
"""

from collections import deque

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        """
            BFS

            Explore every subtree until either leaf reached
            (string not in bank) or end reached

            If end not reached, return -1
        """
        bank = set(bank + [start])
        count = 0

        def get_distance(s1, s2):
            return len([i for i in range(len(s1)) if s1[i] != s2[i]])

        q = deque([(start, 0)])
        while q:
            len_q = len(q)

            for _ in range(len_q):
                curr, mutations = q.popleft()

                if curr not in bank:
                    continue
                bank.remove(curr)

                if curr == end:
                    return mutations

                for string in bank:
                    if get_distance(string, curr) == 1:
                        q.append((string, mutations + 1))
                
        return -1