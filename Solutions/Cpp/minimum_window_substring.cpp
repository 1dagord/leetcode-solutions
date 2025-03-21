/*
    [HARD]
    76. Minimum Window Substring

    Concepts:
    - sliding window
    - hash table

    Stats:
        Runtime | 7 ms      [Beats 69.56%]
        Memory  | 11.27 MB  [Beats 93.62%]
*/

class Solution {
public:
    string minWindow(string s, string t) {
        int m = s.size(), n = t.size();
        if (m < n)
            return "";

        std::unordered_map<char, int> t_count = {};
        for (const char c : t)
            t_count[c]++;

        std::array<int, 2> window = {0, std::numeric_limits<int>::max()};
        int start = 0, finish = n;

        for (int end = 0; end < s.size(); end++) {
            if (t_count[s[end]] > 0)
                finish--;

            t_count[s[end]]--;

            if (!finish) {
                while (t_count[s[start]])
                    t_count[s[start++]]++;

                if (end - start < window[1] - window[0]) {
                    window[0] = start;
                    window[1] = end;
                }

                t_count[s[start]]++;
                finish++;
                start++;
            }
        }

        return (window[1] > m) ?
            ("") :
            (s.substr(window[0], window[1] - window[0] + 1));
    }
};