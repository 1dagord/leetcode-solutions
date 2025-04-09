/*
    [MEDIUM]
    373. Find K Pairs with Smallest Sums

    Concepts:
    - array
    - heap/priority queue

    Stats:
        Runtime | 59 ms     [Beats 62.49%]
        Memory  | 140.08 MB [Beats 63.59%]
*/

class Solution {
public:
    long m, n;

    inline int coords_to_idx(int i, int j) {
        return (i * n) + (j % n);
    }

    vector<vector<int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, long k) {
        /*
            Matrix of pairs

            Run BFS on matrix until k pairs visited
        */
        auto comp = [](const std::array<long, 3>& a, const std::array<long, 3>& b) {
            return a[0] > b[0]; 
        };

        std::priority_queue<
            std::array<long, 3>,
            std::vector<std::array<long, 3>>,
            decltype(comp)
        > q;
        q.push({0, 0, 0});
        std::vector<std::vector<int>> pairs = {};
        std::unordered_set<int> visited = {0};

        int len_queue, ni, nj, idx;
        m = nums1.size(), n = nums2.size();
        const int moves[2][2] = {
            {0, 1},
            {1, 0}
        };

        while (!q.empty()) {
            len_queue = q.size();

            for (int _ = 0; _ < len_queue; _++) {
                auto [__, i, j] = q.top(); q.pop();
                pairs.push_back({nums1[i], nums2[j]});

                if (pairs.size() == std::min(k, m * n))
                    return pairs;

                for (auto [di, dj] : moves) {
                    ni = i + di, nj = j + dj;
                    idx = coords_to_idx(ni, nj);

                    if (ni < m && nj < n && !visited.contains(idx)) {
                        q.push({nums1[ni] + nums2[nj], ni, nj});
                        visited.insert(idx);
                    }
                }
            }
        }

        return pairs;
    }
};