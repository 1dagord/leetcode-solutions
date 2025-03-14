/*
    [MEDIUM]
    238. Product of Array Except Self

    Concepts:
    - array
    - prefix sum

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 42.26 MB  [Beats 16.73%]
*/

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        std::vector<int> pref(n, 1);
        std::vector<int> suff(n, 1);
        std::vector<int> res(n, 1);

        for (int i = 1; i < n; i++)
            pref[i] = pref[i-1] * nums[i-1];

        for (int i = n-2; i > -1; i--)
            suff[i] = suff[i+1] * nums[i+1];

        for (int i = 0; i < n; i++)
            res[i] = pref[i] * suff[i];

        return res;
    }
};