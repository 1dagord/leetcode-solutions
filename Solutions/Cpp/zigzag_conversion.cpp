/*
    [MEDIUM]
    6. Zigzag Conversion

    Concepts:
    - string

    Stats:
        Runtime | 2 ms      [Beats 80.08%]
        Memory  | 14.26 MB  [Beats 39.44%]
*/

class Solution {
public:
    string convert(string s, int num_rows) {
        if (num_rows == 1) return s;

        std::vector<std::string> strs(num_rows);
        bool is_moving_down = true;
        int k = 0;

        for (int i = 0; i < s.length(); i++) {
            strs[k] += s[i];
            k += (is_moving_down) ? (1) : (-1);

            if (k == 0)
                is_moving_down = true;
            else if (k == num_rows - 1)
                is_moving_down = false;
        }
        
        return std::accumulate(strs.begin(), strs.end(), std::string{});
    }
};