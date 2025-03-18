/*
    [MEDIUM]
    56. Merge Intervals

    Concepts:
    - array
    - prefix/suffix sum

    Stats:
        Runtime | 4 ms      [Beats 70.81%]
        Memory  | 23.77 MB  [Beats 80.07%%]
*/

class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        if (intervals.empty()) return {};

        // sort by interval start time
        std::sort(intervals.begin(), intervals.end());
        std::vector<std::vector<int>> res = {};
        res.push_back(intervals[0]);

        for (int i = 1; i < intervals.size(); i++) {
            std::vector<int>& last = res.back();

            // if current interval start before last interval end...
            if (intervals[i][0] <= last[1]) {
                // ...merge last and current
                last[1] = std::max(last[1], intervals[i][1]);
            } else {
                // create new interval
                res.push_back(intervals[i]);
            }
        }

        return res;
    }
};