/*
    [EASY]
    1. Two Sum

    Concepts:
    - hash table

    Stats:
        Runtime | 4 ms      [Beats 60.22%]
        Memory  | 15.75 MB  [Beats 10.19%]
*/

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, std::vector<int>> seen = {};

        for (int i = 0; i < nums.size(); i++) {
            seen[nums[i]].push_back(i);

            if (seen.contains(target - nums[i]) && seen[target - nums[i]][0] != i) {
                if (nums[i] == target - nums[i])
                    return seen[nums[i]];
                else
                    return {seen[nums[i]][0], seen[target - nums[i]][0]};
            }
        }

        return {};
    }
};