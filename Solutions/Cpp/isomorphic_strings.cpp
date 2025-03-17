/*
    [EASY]
    205. Isomorphic Strings

    Concepts:
    - string
    - hash table

    Stats:
        Runtime | 3 ms      [Beats 42.83%]
        Memory  | 9.36 MB   [Beats 54.95%]
*/

class Solution {
public:
    bool isIsomorphic(string a, string b) {
        std::unordered_map<char, char> a_to_b = {};
        std::unordered_map<char, char> b_to_a = {};

        for (int i = 0; i < a.size(); i++) {
            if (!a_to_b.contains(a[i]))
                a_to_b[a[i]] = b[i];
            else if (a_to_b[a[i]] != b[i])
                return false;

            if (!b_to_a.contains(b[i]))
                b_to_a[b[i]] = a[i];
            else if (b_to_a[b[i]] != a[i])
                return false;
        }

        return true;
    }
};