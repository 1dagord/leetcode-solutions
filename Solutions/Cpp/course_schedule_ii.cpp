/*
    [MEDIUM]
    210. Course Schedule II

    Concepts:
    - graph
    - topological sort

    Stats:
        Runtime | 5 ms      [Beats 47.80%]
        Memory  | 19.05 MB  [Beats 19.62%]
*/

class Solution {
public:
    vector<int> findOrder(int n, vector<vector<int>>& prereqs) {
        /*
            Kahn's Algorithm

            https://en.wikipedia.org/wiki/Topological_sorting
        */
        std::unordered_map<int, std::vector<int>> adj = {};
        std::vector<int> indegree(n, 0);
        std::vector<int> res = {};

        int c, p;
        for (std::vector<int> vec : prereqs) {
            // prereq -> course
            c = vec.front(), p = vec.back();
            adj[p].push_back(c);
            indegree[c]++;
        }

        std::deque<int> dq;
        for (int i = 0; i < n; i++) {
            // if no prereqs...
            if (indegree[i] == 0)
                dq.push_back(i);
        }

        // contains courses w/ no prereqs
        int curr;
        while (!dq.empty()) {
            curr = dq.front(); dq.pop_front();
            res.push_back(curr);

            for (int next_course : adj[curr]) {
                indegree[next_course]--;

                // if no more prereqs to be completed...
                if (indegree[next_course] == 0)
                    dq.push_back(next_course);
            }
        }

        // cycle detection
        if (std::accumulate(indegree.begin(), indegree.end(), 0))
            return {};

        // trivial solution: no prereqs
        return res;
    }
};