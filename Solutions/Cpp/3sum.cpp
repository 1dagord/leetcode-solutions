/*
    [MEDIUM]
    15. 3Sum

    Concepts:
    - two pointers
    - sorting

    Stats:
        Runtime | 60 ms     [Beats 30.95%]
        Memory  | 35.32 MB  [Beats 20.82%]
*/

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        std::set<std::vector<int>> triplets = {};
        int n = nums.size();
        int target = 0;
        int j, k;

        std::sort(nums.begin(), nums.end());

        for (int i = 0; i < n; i++) {
            // skip duplicate values
            if (i && nums[i] == nums[i-1])
                continue;

            // set target to be found using other two indices
            target = -nums[i];

            j = i + 1;
            k = n - 1;

            while (j < k) {
                if (nums[j] + nums[k] == target) {
                    triplets.insert({nums[i], nums[j], nums[k]});
                    j++;
                    k--;
                } else if (nums[j] + nums[k] > target) {
                    k--;
                } else {
                    j++;
                }
            }
        }
        
        return std::vector<std::vector<int>>{triplets.begin(), triplets.end()};
    }
};