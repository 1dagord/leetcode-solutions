/*
    [MEDIUM]
    215. Kth Largest Element in an Array

    Concepts:
    - array
    - heap/priority queue

    Stats:
        Runtime | 28 ms     [Beats 64.99%]
        Memory  | 59.27 MB  [Beats 83.03%]
*/

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        int n = nums.size();
        std::make_heap(nums.begin(), nums.end());

        while (!nums.empty() && --k > 0) {
            std::pop_heap(nums.begin(), nums.end());
            if (k > 0) nums.pop_back();
        }

        std::pop_heap(nums.begin(), nums.end());
        return nums.back();
    }
};