/*
    [MEDIUM]
    162. Find Peak Element

    Concepts:
    - array
    - binary search

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 12.33 MB  [Beats 92.26%]
*/

class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int l, m, r;
        l = 0, r = nums.size() - 1;

        while (l < r) {
            m = l + (r - l) / 2;

            if (nums[m] > nums[m+1])
                r = m;
            else
                l = m + 1;
        }

        return l;
    }
};