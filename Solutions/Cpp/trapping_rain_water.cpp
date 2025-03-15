/*
    [HARD]
    42. Trapping Rain Water

    Concepts:
    - array
    - prefix/suffix maximum

    Stats:
        Runtime | 3 ms      [Beats 19.86%]
        Memory  | 27.19 MB  [Beats 40.02%]
*/

class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        int water = 0;

        // prefix and suffix max
        std::vector<int> pref = height;
        std::vector<int> suff = height;

        for (int i = 1; i < n; i++) {
            pref[i] = std::max(pref[i], pref[i-1]);
            suff[n-1-i] = std::max(suff[n-i], suff[n-1-i]);
        }

        // ignore first and last indices
        // as no water can be held here
        for (int i = 1; i < n - 1; i++)
            water += std::min(pref[i], suff[i]) - height[i];
        return water;
    }
};