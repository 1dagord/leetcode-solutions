/*
    [MEDIUM]
    134. Gas Station

    Concepts:
    - array
    - greedy

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 112.23 MB [Beats 94.43%]
*/

class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int n = gas.size();
        int total_tank = 0, tank = 0, left = 0;

        for (int i = 0; i < n; i++) {
            total_tank += gas[i] - cost[i];
            tank += gas[i] - cost[i];
            if (tank < 0) {
                tank = 0;
                left = i + 1;
            }
        }

        return (total_tank >= 0) ? left : -1;
    }
};