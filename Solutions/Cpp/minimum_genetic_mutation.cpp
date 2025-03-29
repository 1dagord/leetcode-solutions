/*
    [MEDIUM]
    433. Minimum Genetic Mutation

    Concepts:
    - string
    - breadth-first search

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 8.93 MB   [Beats 28.97%]
*/

class Solution {
public:
    int get_distance(std::string s1, std::string s2) {
        int diff_count = 0;
        for (int i = 0; i < s1.size(); i++)
            if (s1[i] != s2[i])
                diff_count++;
        return diff_count;
    }
    
    int minMutation(string start, string end, vector<string>& b) {
        /*
            BFS

            Explore every subtree until either leaf reached
            (string not in bank) or end reached

            If end not reached, return -1
        */
        std::unordered_set<std::string> bank(b.begin(), b.end());
        bank.insert(start);
        int count = 0;

        std::queue<std::pair<std::string, int>> q;
        q.push(std::make_pair(start, 0));
        int len_q, mutations;
        std::string curr;

        while (!q.empty()) {
            len_q = q.size();

            for (int _ = 0; _ < len_q; _++) {
                auto [curr, mutations] = q.front();
                q.pop();

                if (!bank.contains(curr))
                    continue;
                bank.erase(curr);

                if (curr == end)
                    return mutations;

                for (std::string str : bank)
                    if (get_distance(str, curr) == 1)
                        q.push({str, mutations + 1});
            }
        }

        return -1;
    }
};