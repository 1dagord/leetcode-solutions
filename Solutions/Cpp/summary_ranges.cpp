/*
    [EASY]
    228. Summary Ranges

    Concepts:
    - array
    - intervals

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 9.40 MB   [Beats 9.78%]
*/

class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        std::vector<std::string> ranges = {};

        if (nums.size() == 0 || nums.size() == 1) {
            for (int num : nums)
                ranges.push_back(std::to_string(num));
            return ranges;
        }

        std::string rng = std::to_string(nums[0]);
        std::string last_num, curr_num;

        for (int i = 1; i < nums.size(); i++) {
            last_num = std::to_string(nums[i-1]);
            curr_num = std::to_string(nums[i]);

            // if discontinuous ranges
            if (0.0 + nums[i] - nums[i-1] != 1) {
                if (rng != last_num)
                    rng += "->" + last_num;
                ranges.push_back(rng);
                rng = curr_num;
            }

            // if at end of list
            if (i == nums.size() - 1) {
                if (rng != curr_num)
                    rng += "->" + curr_num;
                ranges.push_back(rng);
            }
        }

        return ranges;
    }
};