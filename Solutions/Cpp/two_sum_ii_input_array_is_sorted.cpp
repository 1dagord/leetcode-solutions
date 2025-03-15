/*
    [MEDIUM]
    167. Two Sum II - Input Array Is Sorted

    Concepts:
    - array
    - two pointers

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 20.35 MB  [Beats 5.64%]
*/

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int n = numbers.size();
        int left = 0, right = n-1;

        std::vector<int> nums = numbers;
        for (int i = 0; i < nums.size(); i++)
            nums[i] += numbers[0];

        target += *std::min_element(nums.begin(), nums.end());

        while (left < right) {
            if (nums[left] + nums[right] > target)
                right--;
            else if (nums[left] + nums[right] < target)
                left++;
            else
                break;
        }
        return {left + 1, right + 1};
    }
};