/*
    [EASY]
    392. Is Subsequence

    Concepts:
    - string
    - two pointers

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 8.44 MB   [Beats 90.32%]
*/

class Solution {
public:
    bool isSubsequence(string s, string t) {
        auto s_ptr = s.begin(), t_ptr = t.begin();

        while (s_ptr != s.end() && t_ptr != t.end()) {
            if (*s_ptr == *t_ptr)
                s_ptr++;
            t_ptr++;
        }
        return *s_ptr == *(t.end());
    }
};