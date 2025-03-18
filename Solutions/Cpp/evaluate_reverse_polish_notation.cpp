/*
    [MEDIUM]
    150. Evaluate Reverse Polish Notation

    Concepts:
    - stack
    - math

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 17.21 MB  [Beats 20.15%]
*/

class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        std::stack<int> stck = {};
        int a, b;
        const std::unordered_set<std::string> ops = {
            "+", "-", "*", "/"
        };

        for (const std::string c : tokens) {
            if (ops.contains(c)) {
                b = stck.top();
                stck.pop();
                a = stck.top();
                stck.pop();

                if (c == "+")
                    stck.push(a + b);
                else if (c == "-")
                    stck.push(a - b);
                else if (c == "*")
                    stck.push(a * b);
                else
                    stck.push(
                        ((a > 0 && b > 0) || (a < 0 && b < 0)) ?
                        (a / b) :
                        (std::trunc(a / b))   // trunc int division for non-positive result
                    );

            } else {
                stck.push(std::stoi(c));
            }
        }

        return stck.top();
    }
};