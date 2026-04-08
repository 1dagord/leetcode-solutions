/*
    [MEDIUM]
    3653. XOR After Range Multiplication Queries I

    Concepts:
    - array
    - simulation

    Stats:
        Runtime | 53 ms     [Beats 14.29%]
        Memory  | 2.28 MB   [Beats 57.14%]
*/
impl Solution {
    pub fn xor_after_queries(arr: Vec<i32>, queries: Vec<Vec<i32>>) -> i32 {
        let mut nums: Vec<u64> = arr.iter().map(|&x| x as u64).collect();
        const MOD: u64 = (10_u64.pow(9)) + 7;
        for obj in queries {
            let [l, r, k, v] = obj
                .iter()
                .map(|&x| x as usize)
                .collect::<Vec<usize>>()
                .try_into()
                .unwrap();
            for idx in (l..=r).step_by(k) {
                nums[idx] = nums[idx] * v as u64 % MOD;
            }
        }
        return nums.iter().fold(0, |a, b| a ^ b) as i32;
    }
}