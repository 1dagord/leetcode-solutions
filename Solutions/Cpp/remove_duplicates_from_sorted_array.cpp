/*
    [EASY]
    26. Remove Duplicates from Sorted Array

    Concepts:
    - array
    - two pointers

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 21.44 MB  [Beats 86.43%]
*/

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        auto it = unique(nums.begin(), nums.end());
        nums.resize(distance(nums.begin(), it));
        return nums.size();
    }
};