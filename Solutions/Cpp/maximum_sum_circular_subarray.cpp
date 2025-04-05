/*
    [MEDIUM]
    918. Maximum Sum Circular Subarray

    Concepts:
    - array
    - kadane's algorithm

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 43.68 MB  [Beats 49.60%]
*/

class Solution {
public:
    int maxSubarraySumCircular(vector<int>& nums) {
        int curr_max = 0, curr_min = 0;
        int max_sum = std::numeric_limits<int>::min();
        int min_sum = std::numeric_limits<int>::max();

        for (const int num : nums) {
            curr_max = std::max(curr_max + num, num);
            curr_min = std::min(curr_min + num, num);
            max_sum = std::max(curr_max, max_sum);
            min_sum = std::min(curr_min, min_sum);
        }

        return (max_sum > 0) ?
            (
                std::max(
                    max_sum,
                    std::accumulate(nums.begin(), nums.end(), 0) - min_sum
                )
            ) :
            (max_sum);
    }
};