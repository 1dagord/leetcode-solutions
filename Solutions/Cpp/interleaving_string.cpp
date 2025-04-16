/*
    [MEDIUM]
    97. Interleaving String

    Concepts:
    - string
    - dynamic programming

    Stats:
        Runtime | 16 ms     [Beats 22.19%]
        Memory  | 20.76 MB  [Beats 17.99%]
*/

class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        const int n1 = s1.size(), n2 = s2.size(), n3 = s3.size();
        std::map<std::pair<int, int>, bool> cache = {};

        std::function<bool(int, int, std::string)> dfs;
        dfs = [&](int i1, int i2, std::string str){
            if (cache.contains({i1, i2}))
                return cache[{i1, i2}];

            if (i1 == n1 && i2 == n2)
                return str == s3;

            // recurse if either string has next character
            if (i1 < n1 && i1 + i2 < n3 && s1[i1] == s3[i1+i2])
                cache[{i1, i2}] |= dfs(i1+1, i2, str + s1[i1]);
            if (i2 < n2 && i1 + i2 < n3 && s2[i2] == s3[i1+i2])
                cache[{i1, i2}] |= dfs(i1, i2+1, str + s2[i2]);

            return cache[{i1, i2}];
        };

        return dfs(0, 0, "");
    }
};