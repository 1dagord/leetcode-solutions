/*
    [MEDIUM]
    274. H-Index

    Concepts:
    - sorting
    - counting sort

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 12.26 MB  [Beats 66.48%]
*/

class Solution {
public:
    int hIndex(vector<int>& citations) {
        // reverse sort
        std::sort(citations.begin(), citations.end(), std::greater<int>());
        int h_index = 0;
        int num_papers_w_cit = 0;

        for (int i = 0; i < citations.size(); i++) {
            num_papers_w_cit = i + 1;
            h_index = std::max(h_index, std::min(num_papers_w_cit, citations[i]));
        }

        return h_index;
    }
};