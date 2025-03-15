/*
    [HARD]
    135. Candy

    Concepts:
    - array
    - greedy

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 22.87 MB  [Beats 62.15%]
*/

class Solution {
public:
    int candy(vector<int>& ratings) {
        // if adjacent indices, higher gets more candy
        int n = ratings.size();
        std::vector<int> candies(n, 1);
        int lhn = 0, rhn = 0;

        // forward pass
        // if rating higher than LH neighbor, increment
        for (int i = 1; i < n; i++) {
            lhn = ratings[i-1];
            rhn = ratings[i];
            if (lhn < rhn)
                candies[i] = 1 + candies[i-1];
        }

        // backward pass
        // if rating higher than RH neighbor, increment
        for (int i = n-2; i > -1; i--) {
            lhn = ratings[i];
            rhn = ratings[i+1];
            if (lhn > rhn)
                candies[i] = std::max(candies[i], 1 + candies[i+1]);
        }
        return std::reduce(candies.begin(), candies.end(), 0);
    }
};