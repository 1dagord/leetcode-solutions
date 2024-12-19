"""
    [MEDIUM]
    2070. Most Beautiful Item for Each Query

    Concepts:
    - binary search
    - sorting

    Stats:
        Runtime | 196 ms    [Beats 40.52%]
        Memory  | 66.04 MB  [Beats 41.43%]
"""

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        queries = sorted([(q, i) for i, q in enumerate(queries)])

        ans = [0]*len(queries)
        max_b = 0
        j = 0

        # i -> query pointer
        # j -> items pointer
        for q, i in queries:

            while j < len(items) and items[j][0] <= q:
                max_b = max(items[j][1], max_b)
                j += 1

            ans[i] = max_b

        return ans