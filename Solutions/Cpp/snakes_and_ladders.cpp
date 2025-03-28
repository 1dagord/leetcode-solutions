/*
    [MEDIUM]
    909. Snakes and Ladders

    Concepts:
    - matrix
    - breadth-first search

    Stats:
        Runtime | 5 ms      [Beats 42.00%]
        Memory  | 22.41 MB  [Beats 9.29%]
*/

class Solution {
public:
    int n;

    std::array<int, 2> to_coords(int idx) {
        return (
            std::array<int, 2>{
                (n - 1 - (idx / n)),
                ((idx / n) & 1) ?
                (n - 1 - (idx % n)) :
                (idx % n)
            }
        );
    }

    int snakesAndLadders(vector<vector<int>>& board) {
        n = board.size();
        int n_squared = std::pow(n, 2);

        // convert indices to boustrophedon coordinates
        std::unordered_map<int, std::array<int, 2>> idx_to_coords = {};
        for (int i = 0; i < n_squared; i++)
            idx_to_coords[i+1] = to_coords(i);

        // explore board
        std::function<int(void)> bfs;

        bfs = [&]() {
            std::deque<std::pair<int, int>> dq;
            dq.push_back({1, 0});
            std::unordered_set<int> visited = {1};
            int len_q, idx, nidx, moves, i, j;

            while (!dq.empty()) {
                len_q = dq.size();

                for (int _ = 0; _ < len_q; _++) {
                    auto [idx, moves] = dq.front();
                    dq.pop_front();

                    if (idx == n_squared)
                        return moves;

                    for (int didx = 6; didx > 0; didx--) {
                        nidx = idx + didx;
                        if (nidx > n_squared)
                            continue;

                        auto [i, j] = idx_to_coords[nidx];
                        if (board[i][j] != -1)
                            nidx = board[i][j];

                        if (!visited.contains(nidx)) {
                            dq.push_back({nidx, moves + 1});
                            visited.insert(nidx);
                        }
                    }
                }
            }

            return -1;
        };

        return bfs();
    }
};