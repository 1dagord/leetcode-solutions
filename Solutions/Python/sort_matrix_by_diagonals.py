"""
    [MEDIUM]
    3446. Sort Matrix by Diagonals

    Concepts:
    - matrix
    - sorting

    Stats:
        Runtime | 3 ms      [Beats 100%]
        Memory  | 18.07 MB  [Beats 100%]
"""

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        res = [[0]*m for _ in range(n)]

        # store diagonals
        diags = []
        i, j = m - 1, 0
        
        while j < n:
            diag = []
            a, b = i, j
            while 0 <= a < m and 0 <= b < n:
                diag.append(grid[a][b])
                a += 1
                b += 1

            diags.append(diag)

            if i > 0:
                i -= 1
            else:
                j += 1

        # sort diagonals
        is_bottom_left = True
        for d in diags:
            d.sort(reverse=is_bottom_left)
            if is_bottom_left and len(d) == m:
                is_bottom_left = False    

        # rebuild matrix
        i, j = m - 1, 0
        diag_idx = 0

        while j < n:
            a, b = i, j
            idx = 0

            while 0 <= a < m and 0 <= b < n:
                res[a][b] = diags[diag_idx][idx]
                a += 1
                b += 1
                idx += 1
            diag_idx += 1

            if i > 0:
                i -= 1
            else:
                j += 1

        return res