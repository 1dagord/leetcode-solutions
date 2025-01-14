"""
    [MEDIUM]
    2657. Find the Prefix Common Array of Two Arrays

    Concepts:
    - hash table
    - bit manipulation

    Stats:
        Runtime | 27 ms     [Beats 32.72%]
        Memory  | 17.81 MB  [Beats 20.16%]
"""

from collections import defaultdict

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)

        A_count = defaultdict(int)
        B_count = defaultdict(int)
        res = [0]*n

        for i in range(n):
            A_count[A[i]] += 1
            B_count[B[i]] += 1
            res[i] = len(A_count.keys() & B_count.keys())

        return res