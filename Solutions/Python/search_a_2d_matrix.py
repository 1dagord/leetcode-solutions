"""
    [MEDIUM]
    74. Search a 2D Matrix

    Concepts:
    - matrix
    - binary search

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 18.32 MB  [Beats 6.77%]
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left = 0
        right = m * n - 1

        while left <= right:
            mid = (left + right) // 2

            if matrix[mid // n][mid % n] < target:
                left = mid + 1
            elif matrix[mid // n][mid % n] > target:
                right = mid - 1
            else:
                return True

        return False