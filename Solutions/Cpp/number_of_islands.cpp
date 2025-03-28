/*
    [MEDIUM]
    200. Number of Islands

    Concepts:
    - matrix
    - breadth-first search

    Stats:
        Runtime | 39 ms     [Beats 17.03%]
        Memory  | 29.13 MB  [Beats 11.83%]
*/

class Solution {
public:
    int n, m;
    const std::array<const std::array<const int, 2>, 4> moves = {
        std::array<const int, 2>{0, -1},
        std::array<const int, 2>{0, 1},
        std::array<const int, 2>{-1, 0},
        std::array<const int, 2>{1, 0}
    };

    inline int coords_to_idx(int i, int j) {
        return (i * n) + (j % n);
    }
    
    int numIslands(vector<vector<char>>& grid) {
        m = grid.size();
        n = grid[0].size();
        std::unordered_set<int> visited = {};
        int num_islands = 0;

        std::function<void(int, int)> bfs;

        bfs = [&](int row, int col) {
            std::queue<std::array<int, 2>> q;
            q.push({row, col});
            int len_q, ni, nj, idx;

            while (!q.empty()) {
                len_q = q.size();

                for (int _ = 0; _ < len_q; _++) {
                    auto [i, j] = q.front();
                    q.pop();

                    for (auto const [di, dj] : moves) {
                        ni = i + di, nj = j + dj;
                        idx = coords_to_idx(ni, nj);
                        if (
                            0 <= ni && ni < m &&
                            0 <= nj && nj < n &&
                            grid[ni][nj] == '1' &&
                            !visited.contains(idx)
                        ) {
                            q.push({ni, nj});
                            visited.insert(idx);
                        }
                    }
                }
            }
        };

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1' && !visited.contains(coords_to_idx(i, j))) {
                    bfs(i, j);
                    num_islands++;
                }
            }
        }

        return num_islands;
    }
};