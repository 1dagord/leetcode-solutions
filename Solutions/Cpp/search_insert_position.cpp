/*
    [EASY]
    35. Search Insert Position

    Concepts:
    - array
    - binary search

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 13.64 MB  [Beats 42.19%]
*/

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int l, m, r;
        l = 0, r = nums.size() - 1;

        while (l <= r) {
            m = (l + r) / 2;

            if (nums[m] < target)
                l = m + 1;
            else if (nums[m] > target)
                r = m - 1;
            else
                return m;
        }

        return l;
    }
};