"""
    [MEDIUM]
    1861. Rotating the Box

    Concepts:
    - matrix
    - two pointers

    Stats:
        Runtime | 1917 ms   [Beats 45.17%]
        Memory  | 29.21 MB  [Beats 9.52%]
"""

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        """
            1) rotate matrix 90 degrees clockwise
            2) keep pointer of lowest empty space and pointer
                searching for stones
            3) when stone found, swap items at bottom
                and search pointers
        """
        m = len(box)
        n = len(box[0])

        # n rows, m cols
        res = [[0]*m for _ in range(n)]

        for i in range(m):
            for j in range(n):
                res[j][m-1-i] = box[i][j]

        # iterate over all columns
        for j in range(m):
            bottom = n - 1

            # iterate backwards up rows
            i = n - 1
            while i >= 0:
                # if at top of col, break
                if i < 0:
                    break

                # find lowest empty space for bottom
                if res[i][j] == "*":
                    bottom = i - 1

                # swap stone w lowest space and update
                elif res[i][j] == "#":
                    res[i][j], res[bottom][j] = res[bottom][j], res[i][j]
                    bottom -= 1

                i -= 1

        return res
                