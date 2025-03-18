/*
    [MEDIUM]
    71. Simplify Path

    Concepts:
    - stack
    - string

    Stats:
        Runtime | 1 ms      [Beats 73.96%]
        Memory  | 16.20 MB  [Beats 5.23%]
*/

class Solution {
public:
    string simplifyPath(string path) {
        std::vector<std::string> dirs = {};
        std::string word = "";

        // split strings on delimiter '/'
        for (const char c : path) {
            if (c != '/')
                word += c;
            else {
                if (!word.empty()) {
                    dirs.push_back(word);
                    word.clear();
                }
            }
        }

        if (!word.empty())
            dirs.push_back(word);

        std::vector<std::string> stck = {};

        for (const std::string dir : dirs) {
            if (!dir.empty()) {
                if (dir == "..") {
                    if (!stck.empty())
                        stck.pop_back();
                } else if (dir == ".") {
                    continue;
                } else {
                    stck.push_back(dir);
                }
            }
        }

        // equivalent to `"/" + "/".join(stck)`
        return "/" + std::accumulate(
            stck.begin(),
            stck.end(),
            std::string{},
            [](const std::string a, const std::string b){
                return (a.empty()) ? (b) : (a + "/" + b);
            }
        );
    }
};