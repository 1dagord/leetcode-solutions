/*
    [MEDIUM]
    134. Gas Station

    Concepts:
    - array
    - greedy

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 3.32 MB   [Beats 31.82%]
*/
impl Solution {
    pub fn can_complete_circuit(gas: Vec<i32>, cost: Vec<i32>) -> i32 {
        let n: usize = gas.len();
        let (mut total_tank, mut tank, mut left) = (0, 0, 0);

        for i in 0..n {
            total_tank += gas[i] - cost[i];
            tank += gas[i] - cost[i];
            if tank < 0 {
                tank = 0;
                left = i as i32 + 1;
            }
        }

        return if (total_tank >= 0) { left } else { -1 };
    }
}