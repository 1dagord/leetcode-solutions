/*
    [MEDIUM]
    55. Jump Game

    Concepts:
    - array
    - greedy

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 52.30 MB  [Beats 62.30%]
*/

class Solution {
public:
    bool canJump(vector<int>& nums) {
        int goalpost = nums.size() - 1;
        int i = goalpost;

        while (i >= 0) {
            if (goalpost - i <= nums[i])
                goalpost = i;
            i--;
        }
        return (bool)(goalpost == 0);
    }
};