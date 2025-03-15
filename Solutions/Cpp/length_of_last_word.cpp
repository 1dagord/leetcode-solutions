/*
    [EASY]
    58. Length of Last Word

    Concepts:
    - string

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 9.22 MB   [Beats 6.96%]
*/

class Solution {
public:
    int lengthOfLastWord(string s) {
        // trim string
        s.erase(s.find_last_not_of(" \n\r\t") + 1);  
        s.erase(0, s.find_first_not_of(" \n\r\t"));
        return (
            (s.find(" ") != std::string::npos) ?
            (s.substr(s.rfind(" ") + 1, s.length() - 1).length()) :
            (s.length())
        );
    }
};