/*
    [MEDIUM]
    130. Surrounded Regions

    Concepts:
    - matrix
    - depth-first search

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 14.08 MB  [Beats 77.49%]
*/

class Solution {
public:
    int n, m;
    inline bool is_on_edge(int i, int j) {
        return i == 0 || j == 0 || i == m-1 || j == n-1;
    }

    void solve(vector<vector<char>>& board) {
        int ni, nj;
        m = board.size(), n = board[0].size();
        char placeholder = '#';
        const int moves[4][2] = {
            {0, 1},
            {0, -1},
            {1, 0},
            {-1, 0}
        };

        std::function<void(int, int)> dfs;

        dfs = [&](int i, int j){
            board[i][j] = placeholder;
            for (const auto [di, dj] : moves) {
                ni = i + di, nj = j + dj;
                if (
                    0 <= ni && ni < m &&
                    0 <= nj && nj < n &&
                    board[ni][nj] == 'O'
                )
                    dfs(ni, nj);
            }
        };

        // perform dfs from only 'O's on edges
        for (int i = 0; i < m; i++) {
            if (board[i][0] == 'O')
                dfs(i, 0);
            if (board[i][n-1] == 'O')
                dfs(i, n-1);
        }

        for (int j = 0; j < n; j++) {
            if (board[0][j] == 'O')
                dfs(0, j);
            if (board[m-1][j] == 'O')
                dfs(m-1, j);
        }

        // set every non-explored 'O' to an 'X'
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 'O')
                    board[i][j] = 'X';
                else if (board[i][j] == placeholder)
                    board[i][j] = 'O';
            }
        }
    }
};