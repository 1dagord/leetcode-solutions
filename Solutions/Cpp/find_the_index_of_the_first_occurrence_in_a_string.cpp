/*
    [EASY]
    28. Find the Index of the First Occurrence in a String

    Concepts:
    - string
    - string matching

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 8.60 MB   [Beats 82.01%]
*/

class Solution {
public:
    int strStr(string haystack, string needle) {
        return haystack.find(needle);
    }
};