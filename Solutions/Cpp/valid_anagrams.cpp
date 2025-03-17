/*
    [EASY]
    242. Valid Anagram

    Concepts:
    - string
    - hash table

    Stats:
        Runtime | 3 ms      [Beats 54.85%]
        Memory  | 9.81 MB   [Beats 25.97%]
*/

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size())
            return false;
            
        std::unordered_map<char, int> s_cntr = {};
        std::unordered_map<char, int> t_cntr = {};

        for (const char c : s)
            s_cntr[c]++;
        for (const char c : t)
            t_cntr[c]++;

        return s_cntr == t_cntr;
    }
};