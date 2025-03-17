/*
    [MEDIUM]
    49. Group Anagrams

    Concepts:
    - hash table
    - string

    Stats:
        Runtime | 31 ms     [Beats 20.64%]
        Memory  | 26.37 MB  [Beats 27.91%]
*/

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::vector<std::vector<std::string>> res = {};
        std::map<std::string, std::vector<std::string>> groups = {};
        std::string anagram;

        for (std::string s : strs) {
            anagram = s;
            std::sort(anagram.begin(), anagram.end());
            groups[anagram].push_back(s);
        }

        for (const auto [a, _] : groups)
            res.push_back(groups[a]);

        return res;
    }
};