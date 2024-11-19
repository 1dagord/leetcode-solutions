/*
    [MEDIUM]
    2461. Maximum Sum of Distinct Subarrays With Length K

    Concepts:
    - sliding window
    - hash table

    Stats:
        Runtime | 99 ms     [Beats 87.53%]
        Memory  | 108 MB    [Beats 6.87%]
*/

class Solution {
public:
    long long maximumSubarraySum(vector<int>& numbers, int k) {
        // Sliding Window
        int n = numbers.size();
        unsigned long long max_sum = 0;
        unsigned long long curr_sum = 0;
        std::unordered_map<long long, long long> seen;

        // cast to long long
        vector<long long> nums(begin(numbers), end(numbers));

        // initialize map
        for (int i = 0; i < k; i++) {
            curr_sum += nums[i];
            seen[nums[i]]++;
        }

        if (k >= n) {
            return (seen.size() == k) ? (curr_sum) : (0);
        }

        for (int i = 0; i < n - k; i++) {
            // check if distinct
            if (seen.size() == k) max_sum = max(curr_sum, max_sum);

            // update curr sum and seen
            curr_sum += nums[i+k];
            seen[nums[i+k]]++;

            curr_sum -= nums[i];
            seen[nums[i]]--;

            if (!seen[nums[i]]) seen.erase(nums[i]);
        }

        // check final subarray
        if (seen.size() == k) max_sum = max(curr_sum, max_sum);

        return max_sum;
    }
};