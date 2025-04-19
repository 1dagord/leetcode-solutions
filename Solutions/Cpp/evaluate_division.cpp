/*
    [MEDIUM]
    399. Evaluate Division

    Concepts:
    - graph
    - depth-first search

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 12.00 MB  [Beats 53.99%]
*/

class Solution {
public:
    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        const double INF = std::numeric_limits<double>::infinity();
        double val;
        std::vector<double> res(queries.size(), -1.0);
        
        // store nodes and their edge weights
        std::unordered_map<std::string, std::unordered_set<std::string>> nodes = {};
        std::unordered_map<std::string, double> edges = {};
        std::unordered_set<std::string> visited = {};

        std::string num, denom;
        for (int i = 0; i < equations.size(); i++) {
            num = equations[i].front();
            denom = equations[i].back();

            // set edges to self
            nodes[num].insert(num);
            nodes[denom].insert(denom);
            edges[num + "," + num] = 1.0;
            edges[denom + "," + denom] = 1.0;
            // set edges in both directions
            nodes[num].insert(denom);
            nodes[denom].insert(num);
            edges[num + "," + denom] = values[i];
            edges[denom + "," + num] = 1.0 / values[i];
        }

        std::function<bool(std::string, std::string, double)> dfs;
        dfs = [&](std::string node, std::string target, double value) {
            if (!nodes.contains(node))
                return false;

            if (nodes.at(node).contains(target)) {
                val = value * edges.at(node + "," + target);
                return true;
            }

            for (std::string n : nodes.at(node)) {
                if (!visited.contains(n)) {
                    visited.insert(n);
                    if (dfs(n, target, value * edges.at(node + "," + n)))
                        return true;
                    visited.erase(n);
                }
            }

            return false;
        };

        for (int i = 0; i < queries.size(); i++) {
            num = queries[i].front();
            denom = queries[i].back();

            // reset for next iteration
            val = INF;
            visited.clear();
            visited.insert(num);

            dfs(num, denom, 1.0);
            if (val != INF)
                res[i] = val;
        }

        return res;
    }
};