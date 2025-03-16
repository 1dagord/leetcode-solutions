/*
    [MEDIUM]
    11. Container With Most Water

    Concepts:
    - array
    - two pointers

    Stats:
        Runtime | 3 ms      [Beats 35.68%]
        Memory  | 62.87 MB  [Beats 78.85%]
*/

class Solution {
public:
    int maxArea(vector<int>& height) {
        int max_water = 0;
        int n = height.size();
        int left = 0, right = n-1;

        while (left < right) {
            max_water = std::max(
                max_water,
                std::min(
                    height[left],
                    height[right]
                ) * (right - left)
            );

            if (height[left] > height[right])
                right--;
            else
                left++;
        }

        return max_water;
    }
};