/*
    [MEDIUM]
    22. Generate Parentheses

    Concepts:
    - backtracking
    - depth-first search

    Stats:
        Runtime | 11 ms     [Beats 8.46%]
        Memory  | 16.48 MB  [Beats 14.33%]
*/

class Solution {
public:
    vector<string> generateParenthesis(int n) {
        /*
            If we map each parenthesis to a move in a 
            matrix, problem becomes path enumeration from DFS
        */
        std::vector<std::string> paths = {};

        std::function<void(int, int, std::string)> dfs;
        dfs = [&](int i, int j, std::string path){
            if (i == n && j == n)
                paths.push_back(path);

            if (i <= n)
                dfs(i + 1, j, path + "(");
            if (i > j && j <= n)
                dfs(i, j + 1, path + ")");
        };

        dfs(0, 0, "");
        return paths;
    }
};