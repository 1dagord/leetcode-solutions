"""
    [MEDIUM]
    54. Spiral Matrix

    Concepts:
    - matrix
    - simulation

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 16.64 MB  [Beats 91.95%]
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # `i` beholden to `m`
        # `j` beholden to `n`
        visited = set()
        path = []

        m = len(matrix) - 1
        n = len(matrix[0]) - 1

        RIGHT = (1 << 0)    # 1
        DOWN = (1 << 1)     # 2
        LEFT = (1 << 2)     # 4
        UP = (1 << 3)       # 8

        direc = RIGHT
        i, j = 0, 0

        while len(visited) < (m+1) * (n+1):
            if (i, j) not in visited:
                visited.add((i, j))
                path.append(matrix[i][j])

            # move in same direcection until edge or
            # visited square reached, then
            # change direcection
            if direc == RIGHT:
                if j < n and (i, j+1) not in visited:
                    j += 1
                else:
                    # change to DOWN and move down
                    direc = DOWN
                    i += 1
            elif direc == DOWN:
                if i < m and (i+1, j) not in visited:
                    i += 1
                else:
                    # change to LEFT and move left
                    direc = LEFT
                    j -= 1
            elif direc == LEFT:
                if j > 0 and (i, j-1) not in visited:
                    j -= 1
                else:
                    # change to UP and move up
                    direc = UP
                    i -= 1
            elif direc == UP:
                if i > 0 and (i-1, j) not in visited:
                    i -= 1
                else:
                    # change to RIGHT and move right
                    direc = RIGHT
                    j += 1

        return path