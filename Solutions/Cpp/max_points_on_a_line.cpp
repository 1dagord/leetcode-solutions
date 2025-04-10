/*
    [HARD]
    149. Max Points on a Line

    Concepts:
    - math
    - hash table

    Stats:
        Runtime | 64 ms     [Beats 17.94%]
        Memory  | 25.70 MB  [Beats 12.25%]
*/

class Solution {
public:
    int maxPoints(vector<vector<int>>& points) {
        /*
            For each point, calculate angle to every
            other point using inverse tangent

            Store angles in a map
            Return max number of points with same arc tangent
        */

        std::unordered_map<double, double> tangent_map = {};
        double max_points = 1.0;
        double x1, y1, x2, y2, tangent;

        for (std::vector<int> p1 : points) {
            tangent_map.clear();
            for (std::vector<int> p2 : points) {
                // arc tan of same points is zero
                if (p1 == p2)
                    continue;

                x1 = (double)p1[0]; y1 = (double)p1[1];
                x2 = (double)p2[0]; y2 = (double)p2[1];

                tangent = atan2((y2 - y1), (x2 - x1));
                tangent_map[tangent] += 1.0;

                // add 1 to include the point itself
                max_points = std::max(max_points, tangent_map[tangent] + 1.0);
            }
        }

        return (int)max_points;
    }
};