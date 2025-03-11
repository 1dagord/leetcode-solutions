/*
    [EASY]
    169. Majority Element

    Concepts:
    - array
    - hash table

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 28.24 MB  [Beats 24.63%]
*/

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        std::map<int, int> counter = {};
        for (int num : nums) {
            counter[num]++;
            if (counter[num] > nums.size() / 2)
                return num;
        }
        return 0;
    }
};