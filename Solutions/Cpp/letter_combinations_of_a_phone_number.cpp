/*
    [MEDIUM]
    17. Letter Combinations of a Phone Number

    Concepts:
    - backtracking
    - hash table
    - string

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 9.42 MB   [Beats 26.91%]
*/

class Solution {
public:
    vector<string> letterCombinations(string digits) {
        const std::unordered_map<char, const std::string> num_to_let = {
            {'2', "abc"},
            {'3', "def"},
            {'4', "ghi"},
            {'5', "jkl"},
            {'6', "mno"},
            {'7', "pqrs"},
            {'8', "tuv"},
            {'9', "wxyz"}
        };
        // traverse k-ary tree in recursion and
        // loop over first chars in a loop

        std::vector<std::string> combos = {};
        std::function<void(int, std::string)> recurse;

        recurse = [&](int idx, std::string combo){
            // if at leaf, add path
            if (idx == digits.size()) {
                combos.push_back(combo);
                return;
            }

            // add child to path, then call function on child
            for (const char c : num_to_let.at(digits.at(idx)))
                recurse(idx + 1, combo + c);
        };

        if (!digits.empty())
            recurse(0, "");

        return combos;
    }
};