/*
    [EASY]
    290. Word Pattern

    Concepts:
    - string
    - hash table

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 8.97 MB   [Beats 12.31%]
*/

class Solution {
public:
    bool wordPattern(string pattern, string str) {
        std::unordered_set<char> p_set = {};
        std::unordered_set<std::string> s_set = {};
        std::unordered_map<char, std::string> c_to_s = {};

        // split string on spaces
        std::vector<std::string> s;
        std::stringstream ss(str);
        std::string item;

        while (ss >> item)
            s.push_back(item);

        if (pattern.size() != s.size())
            return false;

        for (int i = 0; i < s.size(); i++) {
            if (!c_to_s.contains(pattern[i]))
                c_to_s[pattern[i]] = s[i];
            else if (c_to_s[pattern[i]] != s[i])
                return false;

            p_set.insert(pattern[i]);
            s_set.insert(s[i]);
        }

        return p_set.size() == s_set.size();
    }
};