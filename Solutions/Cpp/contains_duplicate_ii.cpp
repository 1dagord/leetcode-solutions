/*
    [EASY]
    219. Contains Duplicate II

    Concepts:
    - array
    - hash table

    Stats:
        Runtime | 51 ms     [Beats 82.19%]
        Memory  | 81.31 MB  [Beats 27.01%]
*/

class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        std::unordered_map<int, int> idx = {};

        for (int i = 0; i < nums.size(); i++) {
            if (idx.contains(nums[i]) && std::abs(i - idx[nums[i]]) <= k)
                return true;
            idx[nums[i]] = i;
        }

        return false;
    }
};