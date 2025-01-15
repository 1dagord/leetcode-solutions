/*
    [MEDIUM]
    3. Longest Substring Without Repeating Characters

    Concepts:
    - sliding window
    - hash table

    Stats:
        Runtime | 12 ms     [Beats 48.12%]
        Memory  | 20.61 MB  [Beats 9.00%]
*/

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int maxSize = 0;
        int index = 0;
        string noRepeat = "";
        for (auto it = s.begin(); it != s.end(); ++it){
            if (noRepeat.find(*it) != string::npos){
                noRepeat = noRepeat.substr(noRepeat.find(*it)+1);
            }
            noRepeat.push_back(*it);
            maxSize = (noRepeat.size() > maxSize)? noRepeat.size() : maxSize;
        }
        return maxSize;
    }
};