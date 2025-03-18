/*
    [MEDIUM]
    452. Minimum Number of Arrows to Burst Balloons

    Concepts:
    - array
    - greedy
    - sorting

    Stats:
        Runtime | 49 ms     [Beats 56.06%]
        Memory  | 93.95 MB  [Beats 48.63%]
*/

class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        /*
            Find number of overlaps in ranges

            1) sort intervals by start value
            2) check if start of current interval is before
                end of previous
            3) if above is true, overlap (decrement number of arrows)
        */
        std::sort(points.begin(), points.end());
        int n = points.size();

        // max number of arrows is same as number of balloons
        int arrows = n;

        std::array<int, 2> prev = {points[0].front(), points[0].back()};
        std::array<int, 2> curr;
        int s1, s2, e1, e2;

        for (int i = 1; i < n; i++) {
            curr = {points[i].front(), points[i].back()};
            auto [s1, e1] = prev;
            auto [s2, e2] = curr;

            // if overlaps found, decrement number of arrows
            if (s2 <= e1) {
                arrows--;
                prev = {s2, std::min(e1, e2)};
            }

            // otherwise, update previous interval
            else 
                prev = curr;
        }

        return arrows;
    }
};