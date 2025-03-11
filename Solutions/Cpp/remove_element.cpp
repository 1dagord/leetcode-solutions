/*
    [EASY]
    27. Remove Element

    Concepts:
    - array

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 11.57 MB  [Beats 97.68%]
*/

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        for (auto it = nums.begin(); it != nums.end();) {
            if (*it == val) nums.erase(it);
            else it++;
        }
        return nums.size();
    }
};