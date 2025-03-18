/*
    [EASY]
    20. Valid Parentheses

    Concepts:
    - stack
    - string

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 8.78 MB   [Beats 62.78%]
*/

class Solution {
public:
    bool isValid(string s) {
        std::stack<char> stck = {};
        char brack;

        const std::map<char, char> brackets = {
            {'(', ')'},
            {'[', ']'},
            {'{', '}'}
        };

        for (const char c : s) {
            // if c is an opening bracket...
            if (brackets.contains(c))
                stck.push(c);
            else {
                if (stck.empty())
                    return false;
                
                brack = stck.top();
                stck.pop();
                if (c != brackets.at(brack))
                    return false;
            }
        }

        return stck.empty();
    }
};