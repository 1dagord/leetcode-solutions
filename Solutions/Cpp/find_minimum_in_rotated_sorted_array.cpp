/*
    [MEDIUM]
    153. Find Minimum in Rotated Sorted Array

    Concepts:
    - binary search
    - array

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 14.20 MB  [Beats 12.47%]
*/

class Solution {
public:
    int findMin(vector<int>& nums) {
        /*
            Half of array is sorted, other half is rotated

            Identify which half has min, then run Binary Search
        */
        int l, m, r;
        l = 0, r = nums.size() - 1;

        while (l <= r) {
            m = (l + r) / 2;

            // if left val > right val, check mid val
            if (nums[l] > nums[r]) {
                if (nums[m] >= nums[l])
                    l = m + 1;
                else
                    r = m;
            } else {
                return nums[l];
            }
        }

        return nums[r];
    }
};