/*
    [MEDIUM]
    207. Course Schedule

    Concepts:
    - depth-first search
    - graph
    - topological sort

    Stats:
        Runtime | 11 ms     [Beats 25.84%]
        Memory  | 23.12 MB  [Beats 5.75%]
*/

class Solution {
public:
    bool canFinish(int num_courses, vector<vector<int>>& prereqs) {
        std::unordered_map<int, std::vector<int>> graph = {};
        std::unordered_map<int, bool> taken = {};

        for (const std::vector<int> vec : prereqs)
            graph[vec.front()].push_back(vec.back());

        std::function<bool(int)> dfs;

        dfs = [&](int course){
            // if cycle detected...
            if (taken.contains(course))
                return taken[course];

            // assume cannot be taken until all
            // prerequisites are taken
            taken[course] = false;

            for (int pre : graph[course]) {
                // if any prereqs cannot be completed,
                // current course cannot be completed
                if (!dfs(pre))
                    return taken[course];
            }

            taken[course] = true;

            return taken[course];
        };

        for (int course = 0; course < num_courses; course++)
            if (!dfs(course))
                return false;

        return true;
    }
};