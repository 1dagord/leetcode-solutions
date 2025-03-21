/*
    [HARD]
    224. Basic Calculator

    Concepts:
    - stack
    - math
    - string

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 10.65 MB  [Beats 57.27%]
*/

class Solution {
public:
    int calculate(string s) {
        int output = 0;
        int curr = 0, sign = 1;
        std::stack<int> stck = {};

        for (const char c : s) {
            if (isdigit(c)) {
                // account for multi-digit numbers
                curr = curr*10 + (c - '0');
            } else if (c == '+' || c == '-') {
                // store what we calculated so far
                output += curr * sign;
                // reset current sum
                curr = 0;
                // set sign
                sign = (c == '+') ? (1) : (-1);
            } else if (c == '(') {
                // store current output and reset
                stck.push(output);
                output = 0;
                // store current sign and reset
                stck.push(sign);
                sign = 1;
            } else if (c == ')') {
                // add current value
                output += curr * sign;
                // multiply by last stored sign
                output *= stck.top();
                stck.pop();
                // add to last stored sum
                output += stck.top();
                stck.pop();
                // reset current sum
                curr = 0;
            }
        }

        return output + (curr * sign);
    }
};