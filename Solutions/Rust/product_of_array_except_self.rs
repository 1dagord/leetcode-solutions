/*
    [MEDIUM]
    238. Product of Array Except Self

    Concepts:
    - array
    - prefix sum

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 3.88 MB   [Beats 9.74%]
*/
impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        let n: usize = nums.len();
        let mut pref: Vec<i32> = Vec::with_capacity(n);
        for _ in 0..n { pref.push(1); }
        let mut suff: Vec<i32> = pref.clone();
        let mut res: Vec<i32> = pref.clone();

        for i in 1..n {
            pref[i] = pref[i-1] * nums[i-1];
        }
        for i in (0..n-1).rev() {
            suff[i] = suff[i+1] * nums[i+1];
        }
        for i in 0..n {
            res[i] = pref[i] * suff[i];
        }
        
        return res;
    }
}