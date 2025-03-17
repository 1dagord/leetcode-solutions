/*
    [MEDIUM]
    54. Spiral Matrix

    Concepts:
    - matrix
    - simulation

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 9.39 MB   [Beats 50.18%]
*/

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        // `i` beholden to `m`
        // `j` beholden to `n`
        int m = matrix.size() - 1, n = matrix[0].size() - 1;
        std::vector<std::vector<uint8_t>> visited(m+1, std::vector<uint8_t>(n+1, 0));
        std::vector<int> path = {};

        const uint8_t RIGHT = 1 << 0;
        const uint8_t DOWN = 1 << 1;
        const uint8_t LEFT = 1 << 2;
        const uint8_t UP = 1 << 3;

        uint8_t direc = RIGHT;
        int i = 0, j = 0;
        int num_visited = 0;

        while (num_visited < (m+1) * (n+1)) {
            if (visited[i][j] == 0) {
                visited[i][j] = 1;
                path.push_back(matrix[i][j]);
            }

            // move in same direction until edge or
            // visited square reached, then
            // change direction
            switch (direc) {
                case RIGHT:
                    if (j < n && visited[i][j+1] == 0)
                        j++;
                    else {
                        direc = DOWN;
                        i++;
                    }
                    break;

                case DOWN:
                    if (i < m && visited[i+1][j] == 0)
                        i++;
                    else {
                        direc = LEFT;
                        j--;
                    }
                    break;

                case LEFT:
                    if (j > 0 && visited[i][j-1] == 0)
                        j--;
                    else {
                        direc = UP;
                        i--;
                    }
                    break;

                case UP:
                    if (i > 0 && visited[i-1][j] == 0)
                        i--;
                    else {
                        direc = RIGHT;
                        j++;
                    }
                    break;

                default:
                    break;
            }
            num_visited++;
        }

        return path;
    }
};