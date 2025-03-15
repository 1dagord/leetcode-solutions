/*
    [EASY]
    13. Roman to Integer

    Concepts:
    - string
    - hash table

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 13.34 MB  [Beats 35.91%]
*/

class Solution {
public:
    int romanToInt(string s) {
        int n = s.size();
        int num = 0, i = 0;
        std::map<char, int> r_to_i = {
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000}
        };

        while (i < n) {
            if (i < n-1 && r_to_i[s.at(i)] < r_to_i[s.at(i+1)]) {
                num += r_to_i[s.at(i+1)] - r_to_i[s.at(i)];
                i++;
            } else {
                num += r_to_i[s.at(i)];
            }
            i++;
        }
        return num;
    }
};