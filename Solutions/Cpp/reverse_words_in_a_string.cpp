/*
    [MEDIUM]
    151. Reverse Words in a String

    Concepts:
    - string

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 10.53 MB  [Beats 52.85%]
*/

class Solution {
public:
    std::string reverseWords(std::string s) {
        std::string word = "", res = "";
        std::deque<std::string> words = {};

        for (const char c : s) {
            if (c != ' ')
                word += c;
            else {
                if (!word.empty()) {
                    words.push_front(word);
                    word.clear();
                }
            }
        }

        if (!word.empty())
            words.push_front(word);
        for (const std::string w : words)
            res += w + " ";

        res.erase(res.size()-1);
        return res;
    }
};