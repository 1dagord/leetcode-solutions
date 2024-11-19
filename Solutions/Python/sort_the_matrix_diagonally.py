"""
    [MEDIUM]
    1329. Sort the Matrix Diagonally

    Concepts:
    - matrix
    - sorting

    Stats:
        Runtime | 3 ms      [Beats 89.49%]
        Memory  | 17.36 MB  [Beats 13.31%]
"""

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        ans = [[0]*n for _ in range(m)]
        
        # store diagonals
        diags = []
        i = m - 1
        j = 0
        while j < n:
            diag = []
            a, b = i, j
            while 0 <= a < m and 0 <= b < n:
                diag.append(mat[a][b])
                a += 1
                b += 1
            diags.append(diag)
            
            
            if i > 0:
                i -= 1
            else:
                j += 1
                
        # sort diagonals
        for i in range(len(diags)):
            diags[i] = sorted(diags[i])
            
        # rebuild matrix
        i = m - 1
        j = 0
        ind = 0
        while j < n:
            a, b = i, j
            count = 0
            while 0 <= a < m and 0 <= b < n:
                ans[a][b] = diags[ind][count]
                a += 1
                b += 1
                count += 1
            ind += 1
            
            
            if i > 0:
                i -= 1
            else:
                j += 1
                
        return ans