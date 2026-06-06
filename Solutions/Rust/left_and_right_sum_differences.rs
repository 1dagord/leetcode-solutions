/*
    [EASY]
    2574. Left and Right Sum Differences

    Concepts:
    - array
    - prefix sum

    Stats:
        Runtime | 0 s       [Beats 100%]
        Memory  | 2.23 MB   [Beats 41.67%]
*/
impl Solution {
    pub fn left_right_difference(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut pref = nums.clone();
        let mut suff = nums.clone();

        for i in 1..n {
            pref[i] += pref[i - 1];
            suff[n - i - 1] += suff[n - i];
        }

        pref.insert(0, 0);
        suff.push(0);

        suff = Vec::from(&suff[1..]);
        pref.pop();

        return pref
            .iter()
            .zip(suff.iter())
            .map(|(a, b)| (a - b).abs())
            .collect();
    }
}
