/*
    [HARD]
    4. Median of Two Sorted Arrays

    Concepts:
    - sorting
    - binary search

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 95.28 MB  [Beats 48.62%]
*/

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        if (nums1.size() > nums2.size())
            nums1.swap(nums2);

        const int inf = std::numeric_limits<int>::max();
        const int m = nums1.size(), n = nums2.size();
        int l = 0, r = m;
        int part1, part2, max_left_1, min_right_1, max_left_2, min_right_2;

        while (l <= r) {
            part1 = (l + r) / 2;
            part2 = ((m + n + 1) / 2) - part1;

            max_left_1 = (part1 == 0) ? (-inf) : (nums1[part1 - 1]);
            min_right_1 = (part1 == m) ? (inf) : (nums1[part1]);
            max_left_2 = (part2 == 0) ? (-inf) : (nums2[part2 - 1]);
            min_right_2 = (part2 == n) ? (inf) : (nums2[part2]);

            if (max_left_1 <= min_right_2 && max_left_2 <= min_right_1) {
                if ((m + n) & 1)
                    return std::max(max_left_1, max_left_2);
                return (
                    std::max(max_left_1, max_left_2)
                    + std::min(min_right_1, min_right_2)
                ) / 2.0;
            } else if (max_left_1 > min_right_2) {
                r = part1 - 1;
            } else {
                l = part1 + 1;
            }
        }

        return -1;
    }
};