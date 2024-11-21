"""
    [MEDIUM]
    2257. Count Unguarded Cells in the Grid

    Concepts:
    - matrix
    - hash set
    - simulation

    Stats:
        Runtime | 638 ms    [Beats 22.00%]
        Memory  | 48.7 MB   [Beats 14.62%]
"""

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        """
            Keep count of all non-guarded cells

            Iterate over guards and extend in every direction
            until another guard or wall reached
        """
        count = m * n - len(walls)

        guards = set([tuple(g) for g in guards])
        walls = set([tuple(w) for w in walls])
        visited = set()

        for row, col in guards:
            # update count
            count -= 1

            if (row, col) in visited:
                continue
            visited.add((row, col))

            # extend guard in all directions
            for di, dj in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                i, j = row, col
                while (0 <= (ni := i + di) < m and
                        0 <= (nj := j + dj) < n and
                        (ni, nj) not in guards):

                        # update i and j
                        i, j = ni, nj

                        if (i, j) in walls:
                            break
                        if (i, j) in visited:
                            continue

                        # update board and visited
                        count -= 1
                        visited.add((i, j))


        return count