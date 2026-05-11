/*
    [EASY]
    2553. Separate the Digits in an Array

    Concepts:
    - array
    - simulation

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.28 MB   [Beats 52.63%]
*/
impl Solution {
    pub fn separate_digits(nums: Vec<i32>) -> Vec<i32> {
        let mut answer: Vec<i32> = Vec::new();
        let mut digits: Vec<i32> = Vec::new();

        for mut num in nums {
            while num > 0 {
                digits.push(num % 10);
                num /= 10;
            }
            digits.reverse();
            answer.append(&mut digits);
        }

        return answer;
    }
}