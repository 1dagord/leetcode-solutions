/*
    [EASY]
    383. Ransom Note

    Concepts:
    - string
    - hash table

    Stats:
        Runtime | 3 ms      [Beats 62.48%]
        Memory  | 11.90 MB  [Beats 29.56%]
*/

class Solution {
public:
    bool canConstruct(string ransom_note, string magazine) {
        std::unordered_map<char, int> r_count = {};
        std::unordered_map<char, int> m_count = {};

        for (const char c : ransom_note)
            r_count[c]++;
        for (const char c : magazine)
            m_count[c]++;

        for (const auto [k, v] : r_count) {
            if (!(m_count.contains(k) && m_count[k] >= v))
                return false;
        }

        return true;
    }
};