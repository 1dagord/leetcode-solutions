/*
    [MEDIUM]
    289. Game of Life

    Concepts:
    - matrix
    - simulation

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 9.50 MB   [Beats 61.32%]
*/

class Solution {
public:
    void gameOfLife(vector<vector<int>>& board) {
        /*
            < 2 live neighbors: dies
            2-3 live neighbors: survives
            >3 live neighbors: dies
            dead w 3 live neighbors: revived
        */
        int m = board.size(), n = board[0].size();
        int live_neighbors = 0;
        int ni, nj;

        std::vector<std::vector<int>> next_state = board;
        const std::vector<std::array<int, 2>> moves = {
            {-1, -1},
            {-1, 0},
            {-1, 1},
            {0, -1},
            {0, 1},
            {1, -1},
            {1, 0},
            {1, 1},
        };

        // get next state
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {

                // get number of live neighbors
                live_neighbors = 0;
                for (auto [di, dj] : moves) {
                    ni = i + di;
                    nj = j + dj;
                    if (
                        0 <= ni && ni < m &&
                        0 <= nj && nj < n &&
                        board[ni][nj] != 0
                    )
                        live_neighbors++;
                }

                // if current cell is live...
                if (board[i][j] != 0) {
                    if (
                        live_neighbors < 2 ||
                        live_neighbors > 3
                    )
                        next_state[i][j] = 0;
                    else if (live_neighbors == 2 || live_neighbors == 3)
                            next_state[i][j] = 1;
                }
                // if current cell is dead...
                else {
                    if (live_neighbors == 3)
                        next_state[i][j] = 1;
                }
            }
        }

        // update board
        for (int i = 0; i < m; i++)
            board[i] = next_state[i];
    }
};