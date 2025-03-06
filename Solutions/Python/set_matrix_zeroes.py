"""
    [MEDIUM]
    73. Set Matrix Zeroes

    Concepts:
    - matrix

    Stats:
        Runtime | 8 ms      [Beats 11.33%]
        Memory  | 17.39 MB  [Beats 100%]
"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        # set marked elements to None
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != None and matrix[i][j] == 0:
                    for row in range(m):
                        if row != i and matrix[row][j] != 0:
                            matrix[row][j] = None
                    for col in range(n):
                        if col != j and matrix [i][col] != 0:
                            matrix[i][col] = None

        # set None elements to 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == None:
                    matrix[i][j] = 0