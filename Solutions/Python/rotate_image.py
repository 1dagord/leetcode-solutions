"""
    [MEDIUM]
    48. Rotate Image

    Concepts:
    - matrix
    - math

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 16.71 MB  [Beats 86.61%]
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        rot_mat = [[None]*n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                rot_mat[j][i] = matrix[i][j]

        for i in range(n):
            for j in range(n):
                matrix[i][j] = rot_mat[i][n-j-1]