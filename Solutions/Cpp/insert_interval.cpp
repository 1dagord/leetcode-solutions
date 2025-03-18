/*
    [MEDIUM]
    57. Insert Interval

    Concepts:
    - array

    Stats:
        Runtime | 3 ms      [Beats 30.94%]
        Memory  | 21.52 MB  [Beats 94.25%]

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