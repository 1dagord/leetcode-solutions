"""
    [MEDIUM]
    2017. Grid Game

    Concepts:
    - matrix
    - prefix sum

    Stats:
        Runtime | 194 ms    [Beats 5.25%]
        Memory  | 30.74 MB  [Beats 9.84%]
"""

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        """
            Both robots want to take path with most points
            Can only move right and down

            First robot will divide remaining board into two
            groups of cells

            Goal of first robot is to minimize sum of values
            in both cells
        """
        n = len(grid[0])

        # prefix sum
        pref = [[num for num in [0] + row] for row in grid]
        for j in range(2, n+1):
            for i in range(2):
                pref[i][j] += pref[i][j-1]

        res = float("inf")

        for i in range(1, n+1):
            # sums of top and bottom remaining regions
            top = pref[0][-1] - pref[0][i]
            bottom = pref[1][i-1]

            # second robot will collect largest
            second_robot = max(top, bottom)
            res = min(res, second_robot)

        return res