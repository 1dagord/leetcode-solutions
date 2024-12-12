/*
    [EASY]
    2558. Take Gifts From the Richest Pile

    Concepts:
    - heap/priority queue

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 13.60 MB  [Beats 7.74%]
*/

class Solution {
public:
    long long pickGifts(vector<int>& gifts, int k) {
        std::priority_queue<long> pq(gifts.begin(), gifts.end());
        long long sum = 0;
        int val = 0;

        while (k != 0) {
            val = pq.top();
            pq.pop();
            pq.push(std::floor(std::sqrt(val)));
            k--;
        }

        for (; !pq.empty(); pq.pop())
            sum += pq.top();
        return sum;
    }
};