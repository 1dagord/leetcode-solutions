/*
    [MEDIUM]
    12. Integer to Roman

    Concepts:
    - string
    - hash table

    Stats:
        Runtime | 11 ms     [Beats 12.34%]
        Memory  | 17.55 MB  [Beats 5.04%]
*/

class Solution {
public:
    string intToRoman(int num) {
        std::map<int, std::string, std::greater<int>> roman_nums = {
            {1000, "M"},
            {900, "CM"},
            {500, "D"},
            {400, "CD"},
            {100, "C"},
            {90, "XC"},
            {50, "L"},
            {40, "XL"},
            {10, "X"},
            {9, "IX"},
            {5, "V"},
            {4, "IV"},
            {1, "I"}
        };

        std::string roman = "";
        std::map<int, int, std::greater<int>> roman_count = {};

        for (const auto [k, v] : roman_nums) {
            while (num >= k) {
                roman_count[k]++;
                num -= k;
            }
        }

        for (const auto [k, v] : roman_count) {
            for (int i = 0; i < v; i++)
                roman.append(roman_nums[k]);
        }

        return roman;
    }
};