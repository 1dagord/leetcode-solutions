/*
    [EASY]
    125. Valid Palindrome

    Concepts:
    - string
    - two pointers

    Stats:
        Runtime | 3 ms      [Beats 32.21%]
        Memory  | 10.29 MB  [Beats 27.99%]
*/

class Solution {
public:
    bool isPalindrome(string s) {
        std::vector<char> vec = {};
        for (char c : s) {
            if (std::isalnum(c))
                vec.push_back(tolower(c));
        }

        int n = vec.size();
        for (int i = 0; i < (n + 1) / 2; i++) {
            if (vec[i] != vec[n - i - 1])
                return false;
        }
        return true;
    }
};