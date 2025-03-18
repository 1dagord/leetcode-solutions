/*
    [MEDIUM]
    56. Merge Intervals

    Concepts:
    - array
    - prefix/suffix sum

    Stats:
        Runtime | 13 ms     [Beats 11.27%]
        Memory  | 27.11 MB  [Beats 5.01%]
*/

class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        int n = 0;
        for (std::vector<int> row : intervals)
            for (int item : row)
                n = std::max(item, n);

        std::vector<std::vector<int>> res = {};
        std::unordered_set<int> singles = {};   // length-1 intervals
        std::vector<int> pref(n+1, 0);
        std::vector<int> suff(n+1, 0);

        // mark start and end of each interval
        for (const std::vector<int> row : intervals) {
            const auto& [start, end] = std::array<int, 2>{row.front(), row.back()};
            if (start == end)
                singles.insert(start);

            pref[start]++;
            pref[end]--;
            suff[end]++;
            suff[start]--;
        }

        // run prefix and suffix sum on overlaps
        for (int i = 1; i < pref.size(); i++) {
            pref[i] += pref[i-1];
            suff[n-i] += suff[n-i+1];
        }

        // store merged intervals
        std::vector<int> rng = {};
        for (int i = 0; i < pref.size(); i++) {
            if (pref[i] > 0 && suff[i] == 0) {
                // begin interval
                rng.clear();
                rng.push_back(i);
            } else if (pref[i] == 0 && suff[i] > 0) {
                // end interval
                rng.push_back(i);
                res.push_back(rng);
                rng.clear();
            } else if (pref[i] == 0 && suff[i] == 0) {
                if (singles.contains(i))
                    res.push_back({i, i});
            }
        }

        return res;
    }
};