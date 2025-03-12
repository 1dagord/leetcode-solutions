/*
    [MEDIUM]
    189. Rotate Array

    Concepts:
    - array

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 29.48 MB  [Beats 79.98%]
*/

class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        std::rotate(nums.begin(), nums.begin() + (n - (k % n)), nums.end());
    }
};