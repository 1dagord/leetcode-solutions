/*
    [MEDIUM]
    128. Longest Consecutive Sequence

    Concepts:
    - array
    - hash table

    Stats:
        Runtime | 99 ms     [Beats 23.75%]
        Memory  | 88.88 MB  [Beats 24.09%]
*/

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int length = 0;
        std::unordered_set<int> vals{nums.begin(), nums.end()};
        int val, lo, hi;

        while (!vals.empty()) {
            auto it = vals.begin();
            val = *it;
            vals.erase(it);

            lo = val, hi = val;
            while (vals.contains(lo - 1)) 
                vals.erase(lo-- - 1);

            while (vals.contains(hi + 1)) 
                vals.erase(hi++ + 1);

            length = std::max(hi - lo + 1, length);
        }

        return length;
    }
};