/*
    [MEDIUM]
    79. Word Search

    Concepts:
    - matrix
    - depth-first search
    - backtracking

    Stats:
        Runtime | 416 ms    [Beats 50.55%]
        Memory  | 49.46 MB  [Beats 9.80%]
*/

class Solution {
public:
    const int moves[4][2] = {
        {0, 1},
        {0, -1},
        {1, 0},
        {-1, 0}
    };

    int coords_to_idx(int i, int j, int n) {
        return ((i * n) + j);
    }

    bool exist(vector<vector<char>>& board, string word) {
        /*
            DFS w/ Search Pruning

            We can automatically eliminate words that do not
            meet either of the following two criteria

            1) len(word) >= m * n
            2) count for chars in word <= count for chars in board
        */
        const int m = board.size(), n = board[0].size();
        std::unordered_set<int> visited = {};

        if (m == 1 && n == 1)
            return word == std::string{board[0][0]};

        std::function<bool(int, int, int, std::string)> dfs;
        dfs = [&](
            int i,
            int j,
            int idx,
            std::string substr
        ) {
            bool outcome = false;

            if (substr == word)
                return true;

            for (auto [di, dj] : moves) {
                int ni = i + di, nj = j + dj;
                if (
                    0 <= ni && ni < m &&
                    0 <= nj && nj < n &&
                    !visited.contains(coords_to_idx(ni, nj, n)) &&
                    idx < word.size() - 1 &&
                    board[ni][nj] == word[idx + 1]
                ) {
                    visited.insert(coords_to_idx(ni, nj, n));
                    outcome |= dfs(
                        ni,
                        nj,
                        idx + 1,
                        substr + board[ni][nj]
                    );
                    visited.erase(coords_to_idx(ni, nj, n));
                }
            }

            return outcome;
        };

        // prune searched based on length
        if (word.size() > m * n)
            return false;

        // prune searches based on char frequency
        std::unordered_map<char, int> board_counter = {};
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                board_counter[board[i][j]]++;

        std::unordered_map<char, int> word_counter = {};
        for (char c : word)
            word_counter[c]++;

        for (auto [c, count] : word_counter)
            if (!board_counter.contains(c) || board_counter.at(c) < count)
                return false;
            
        // run dfs
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == word[0]) {
                    visited.clear();
                    visited.insert(coords_to_idx(i, j, n));
                    if ( 
                        dfs(
                            i,
                            j,
                            0,
                            std::string{word[0]}
                        )
                    ) {
                        return true;
                    }
                }
            }
        }

        return false;
    }
};