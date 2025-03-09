/*
    [EASY]
    88. Merge Sorted Array

    Concepts:
    - array
    - two pointers

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 12.20 MB  [Beats 70.67%]
*/

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int i = 0, j = 0;
        while (i < m + n && j < n) {
            if (nums1[i] > nums2[j]) {
                nums1.insert(nums1.begin() + i, nums2[j]);
                j++;
            }
            else {
                i++;
            }
        }
        while (j < n) {
            nums1.insert(nums1.begin() + m + j, nums2[j]);
            j++;
        }
        nums1.erase(nums1.begin() + m + n, nums1.end());
    }
};