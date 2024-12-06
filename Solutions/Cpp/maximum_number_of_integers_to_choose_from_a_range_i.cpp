/*
    [MEDIUM]
    2554. Maximum Number of Integers to Choose From a Range I

    Concepts:
    - array
    - hash table

    Stats:
        Runtime | 203 ms    [Beats 46.18%]
        Memory  | 183.88 MB [Beats 31.21%]
*/

class Solution {
public:
    int maxCount(vector<int>& banned, int n, int max_sum) {
        unordered_set<int> bnnd(banned.begin(), banned.end());
        vector<int> nums = {};

        for (int i = 1; i <= n; i++)
            if (!bnnd.contains(i))
                nums.push_back(i);

        int curr_sum = 0;
        for (int num : nums)
            curr_sum += num;

        int amt_nums = nums.size();

        while (curr_sum > max_sum)
            curr_sum -= nums.at(--amt_nums);

        return amt_nums;
    }
};