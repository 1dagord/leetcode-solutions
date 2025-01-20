"""
    [MEDIUM]
    2661. First Completely Painted Row or Column

    Concepts:
    - matrix
    - hash table

    Stats:
        Runtime | 108 ms    [Beats 85.80%]
        Memory  | 51.78 MB  [Beats 54.57%]
"""

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        val_to_coord = {}

        # map values to coordinates in grid
        for i, row in enumerate(mat):
            for j, item in enumerate(row):
                val_to_coord[item] = (i, j)

        # count of painted cells in each row and column
        row_count = [0]*m
        col_count = [0]*n

        for idx, val in enumerate(arr):
            i, j = val_to_coord[val]

            # increment number of painted cells
            row_count[i] += 1
            col_count[j] += 1
            
            # check for completely painted rows and columns
            if row_count[i] == n or col_count[j] == m:
                return idx

        return -1
            