/*
    [MEDIUM]
    167. Two Sum II - Input Array Is Sorted

    Concepts:
    - array
    - two pointers

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.48 MB   [Beats 2.63%]
*/
impl Solution {
    pub fn two_sum(numbers: Vec<i32>, mut target: i32) -> Vec<i32> {
        let n = numbers.len();
        let [mut left, mut right] = [0, n - 1];

        let mut nums = numbers.clone();
        for i in 0..n { nums[i] += numbers[0]; }

        target += *nums.iter().min().unwrap();

        while left < right {
            if nums[left] + nums[right] > target {
                right -= 1;
            } else if nums[left] + nums[right] < target {
                left += 1;
            } else {
                break;
            }
        }

        return vec![left as i32 + 1, right as i32 + 1];
    }
}