/*
    [MEDIUM]
    2337. Move Pieces to Obtain a String

    Concepts:
    - string

    Stats:
        Runtime | 39 ms     [Beats 14.37%]
        Memory  | 50.61 MB  [Beats 5.40%]
*/

class Solution {
public:
    bool canChange(string start, string target) {
        vector<pair<int, char>> s_chars = {};
        vector<pair<int, char>> t_chars = {};

        for (int i = 0; i < start.size(); i++) {
            if (start.at(i) == 'L' || start.at(i) == 'R')
                s_chars.push_back(pair(i, start.at(i)));
            if (target.at(i) == 'L' || target.at(i) == 'R')
                t_chars.push_back(pair(i, target.at(i)));
        }

        if (s_chars.size() != t_chars.size()) return false;

        int si, ti;
        char sx, tx;
        for (int i = 0; i < s_chars.size(); i++) {
            auto [si, sx] = s_chars[i];
            auto [ti, tx] = t_chars[i];

            if (sx != tx) return false;

            if (sx == 'L') {
                if (ti > si)
                    return false;
            } else if (sx == 'R') {
                if (ti < si)
                    return false;
            }
        }

        return true;
    }
};