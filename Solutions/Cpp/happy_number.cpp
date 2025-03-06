/*
    [EASY]
    202. Happy Number

    Concepts:
    - math
    - hash table

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 5.72 MB   [Beats 100%]
*/

class Solution {
public:
    bool isHappy(int n) {
        int originalNum = n;
        while (n > 3){
            string nStr = std::to_string(n);
            int runningSum = 0;
            for (char &it : nStr){
                runningSum += pow((int)(it-'0'), 2);
            }
            if (runningSum == 1) return true;
            if (n == 4 || n == 5) return false;
            n = runningSum;
        }
        return n == 1;
    }
};