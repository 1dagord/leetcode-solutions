/*
    [MEDIUM]
    209. Minimum Size Subarray Sum

    Concepts:
    - array
    - sliding window

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 31.92 MB  [Beats 96.97%]
*/

class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        /*
            1) keep track of window through two pointers
            2) grow window by incrementing right pointer
            3) if window sum exceeds target, decrease window
                size from left and continue
        */
        int n = nums.size();
        int min_len = n+1;
        int left = 0, curr_sum = 0;

        for (int right = 0; right < n; right++) {
            curr_sum += nums[right];

            // if sum >= target...
            while (curr_sum >= target) {
                // update min_len
                if (right - left + 1 < min_len)
                    min_len = right - left + 1;

                // decrease sum and window size from left
                curr_sum -= nums[left];
                left++;
            }
        }

        return (min_len < n+1) ? (min_len) : (0);
    }
};