"""
    [MEDIUM]
    1072. Flip Columns For Maximum Number of Equal Rows

    Concepts:
    - matrix
    - hash table

    Stats:
        Runtime | 50 ms     [Beats 65.28%]
        Memory  | 19.83 MB  [Beats 45.59%]
"""

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        """
            Instead of flipping columns, compare patterns
            of rows so that inverted rows map to same output
        """
        mp = defaultdict(int)
        for row in matrix:
            key = tuple([val == row[0] for val in row])
            mp[key] += 1

        return max(mp.values())