/*
    [HARD]
    212. Word Search II

    Concepts:
    - matrix
    - trie
    - depth-first search

    Stats:
        Runtime | 1179 ms   [Beats 20.73%]
        Memory  | 20.69 MB  [Beats 31.62%]
*/

class TrieNode {
public:
    std::unordered_map<char, TrieNode*> nodes;
    bool is_leaf, word_found;

    TrieNode() {
        nodes = {};
        is_leaf = false;
        word_found = false;
    }

    bool search(string word) {
        TrieNode* curr = this;

        for (const char c : word) {
            if (!curr->nodes.contains(c))
                return false;
            curr = curr->nodes[c];
        }
        return curr->is_leaf;
    }
};

class Solution {
public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        /*
            Build trie, search trie and
            matrix using DFS
        */
        const int m = board.size(), n = board[0].size();
        const int moves[4][2] = {
            {0, 1},
            {0, -1},
            {1, 0},
            {-1, 0}
        };

        std::vector<std::string> words_on_board = {};
        TrieNode* root = new TrieNode();
        TrieNode* curr;

        // populate trie
        for (const std::string word : words) {
            curr = root;

            for (const char c : word) {
                if (!curr->nodes.contains(c))
                    curr->nodes[c] = new TrieNode();
                curr = curr->nodes[c];
            }
            curr->is_leaf = true;
        }

        std::vector<std::vector<bool>> visited(m, std::vector<bool>(n, false));
        std::function<void(int, int, std::string, TrieNode*)> dfs;

        dfs = [&](int i, int j, std::string path, TrieNode* curr){
            /*
                Performs DFS on board while using
                trie for guidance
            */
            if (curr->is_leaf && !curr->word_found) {
                words_on_board.push_back(path);
                curr->word_found = true;
            }

            for (const auto [di, dj] : moves) {
                int ni = i + di;
                int nj = j + dj;
                if (
                    0 <= ni && ni < m &&
                    0 <= nj && nj < n &&
                    !visited[ni][nj] &&
                    curr->nodes.contains(board[ni][nj])
                ) {
                    visited[ni][nj] = true;
                    dfs(ni, nj, path + board[ni][nj], curr->nodes[board[ni][nj]]);
                    visited[ni][nj] = false;
                }
            }
        };

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (root->nodes.contains(board[i][j])) {
                    visited = std::vector(m, std::vector<bool>(n, false));
                    visited[i][j] = true;
                    dfs(i, j, std::string{board[i][j]}, root->nodes[board[i][j]]);
                }
            }
        }

        return words_on_board;
    }
};