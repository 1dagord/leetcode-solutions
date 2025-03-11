/*
    [MEDIUM]
    80. Remove Duplicates from Sorted Array II

    Concepts:
    - array
    - two pointers

    Stats:
        Runtime | 7 ms      [Beats 54.99%]
        Memory  | 19.60 MB  [Beats 35.16%]
*/

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size() <= 2) return nums.size();
        
        int k = 2;
        for (int i = 2; i < nums.size(); i++) {
            if (nums[i] != nums[k-2]) {
                nums[k] = nums[i];
                k++;
            }
        }
        return k;
    }
};