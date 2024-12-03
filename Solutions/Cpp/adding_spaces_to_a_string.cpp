/*
    [MEDIUM]
    2109. Adding Spaces to a String

    Concepts:
    - string
    - two pointers

    Stats:
        Runtime | 19 ms     [Beats 63.55%]
        Memory  | 85.42 MB  [Beats 19.63%]
*/

class Solution {
public:
    string addSpaces(string s, vector<int>& spaces) {
        int n = s.size();
        int k = spaces.size();

        int i = 0;
        int j = 0;

        string res;

        while (j < n) {
            if (i < k && j == spaces.at(i)) {
                // string& append(const char* c)
                res.append(" ");
                i++;
            } else {
                // void push_back (char c)
                res.push_back(s.at(j));
                j++;
            }
        }

        return res;
    }
};