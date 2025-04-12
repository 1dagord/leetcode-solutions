/*
    [MEDIUM]
    5. Longest Palindromic Substring

    Concepts:
    - string
    - two pointers

    Stats:
        Runtime | 965 ms    [Beats 8.39%]
        Memory  | 472.56 MB [Beats 5.01%]
*/

class Solution {
public:
    string longestPalindrome(string s) {
        /*
            Treat current char as center of palindrome
            and expand outward until edges reached or
            substring not a palindrome
        */
        const int n = s.size();
        std::string longest, odd, even;
        longest = "";

        std::function<std::string(int, int)> expand;
        expand = [&](int left, int right){
            std::string palindrome = "";

            while (left >= 0 && right < n && s[left] == s[right]) {
                palindrome = s.substr(left, right - left + 1);
                left--;
                right++;
            }

            return palindrome;
        };

        for (int i = 0; i < n; i++) {
            odd = expand(i, i);
            even = expand(i, i+1);

            if (odd.size() > longest.size())
                longest = odd;
            if (even.size() > longest.size())
                longest = even;
        }

        return longest;
    }
};