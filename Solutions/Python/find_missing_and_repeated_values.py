"""
    [MEDIUM]
    2965. Find Missing and Repeated Values

    Concepts:
    - hash table
    - math

    Stats:
        Runtime | 7 ms      [Beats 72.80%]
        Memory  | 18.40 MB  [Beats 23.37%]
"""

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        n_sq = n ** 2
        counter = Counter([val for row in grid for val in row])
        repeated = counter.most_common(1)[0][0]
        missing = (((n_sq + 1) * (n_sq)) // 2) - sum(counter)

        return [repeated, missing]