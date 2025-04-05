/*
    [MEDIUM]
    33. Search in Rotated Sorted Array

    Concepts:
    - binary search
    - array

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 15.30 MB  [Beats 33.79%]
*/

class Solution {
public:
    int search(vector<int>& nums, int target) {
        /*
            Divide array into strictly increasing part and pivoted part
            Decide which part target is in
            Run Binary Search on that part
        */
        int left, mid, right;
        left = 0, right = nums.size() - 1;

        while (left <= right) {
            mid = (left + right) / 2;

            if (nums[mid] == target)
                return mid;

            // if left half is sorted...
            if (nums[left] <= nums[mid]) {
                // and target is inside sorted left half...
                if (nums[left] <= target && target < nums[mid])
                    right = mid - 1;
                else
                    left = mid + 1;
            } else {
                if (nums[mid] < target && target <= nums[right])
                    left = mid + 1;
                else
                    right = mid - 1;
            }
        }

        return -1;
    }
};