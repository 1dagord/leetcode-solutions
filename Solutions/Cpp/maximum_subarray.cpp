/*
    [MEDIUM]
    53. Maximum Subarray

    Concepts:
    - array

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 71.74 MB  [Beats 53.49%]
*/

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        /*
            Kadane's Algorithm

            While iterating over array, each position
            offers two choices:
            
            1) extend subarray by adding current value
            2) begin new subarray at current value

            If current sum ending at previous index < 0,
            begin new subarray at current index
        */
        int curr_sum = 0, max_sum = std::numeric_limits<int>::min();

        for (int i = 0; i < nums.size(); i++) {
            curr_sum = std::max(curr_sum + nums[i], nums[i]);
            max_sum = std::max(max_sum, curr_sum);
        }
        
        return max_sum;
    }
};