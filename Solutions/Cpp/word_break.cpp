/*
    [MEDIUM]
    139. Word Break

    Concepts:
    - string
    - dynamic programming

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 10.36 MB  [Beats 89.85%]
*/

class Solution {
public:
    bool wordBreak(string s, vector<string>& word_list) {
        const int n = s.size();
        int word_len;
        // store true at dp[i] if s[i:] contains words in dictionary
        std::vector<bool> dp(n+1, false);
        // if at end of string, true
        dp[n] = true;

        for (int i = n - 1; i > -1; i--) {
            for (std::string word : word_list) {
                word_len = word.size();
                // if `word` first in substring starting at `i` and
                // can find word starting at index `i`...
                if (i + word_len <= n && s.substr(i, word_len) == word) {
                    // set dp[i] equal to value of dp `word_len` letters ahead
                    dp[i] = dp[i + word_len];
                }
                if (dp[i])
                    break;
            }
        }

        return dp[0];
    }
};