/*
    [MEDIUM]
    34. Find First and Last Position of Element in Sorted Array

    Concepts:
    - array
    - binary search

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 17.49 MB  [Beats 86.77%]
*/

class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        std::function<int(bool)> binary_search;
        binary_search = [&](bool is_increasing) {
            int l, m, r, occ;
            l = 0, r = nums.size() - 1;
            occ = -1;

            while (l <= r) {
                m = l + (r - l) / 2;

                if (nums[m] < target)
                    l = m + 1;
                else if (nums[m] > target)
                    r = m - 1;
                else {
                    occ = m;
                    // if array is increasing...
                    if (is_increasing) {
                        // continue searching left
                        r = m - 1;
                    } else {
                        // continue searching right
                        l = m + 1;
                    }
                }
            }

            return occ;
        };

        int first = binary_search(true);
        if (first != -1)
            return {first, binary_search(false)};
        return {-1, -1};
    }
};