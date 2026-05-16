/*
    [HARD]
    224. Basic Calculator

    Concepts:
    - stack
    - math
    - string

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.49 MB   [Beats 82.76%]
*/
impl Solution {
    pub fn calculate(s: String) -> i32 {
        let mut output: i32 = 0;
        let [mut curr, mut sign]: [i32; 2] = [0, 1];
        let mut stack: Vec<i32> = Vec::new();

        for c in s.chars() {
            if c.is_digit(10) {
                // account for multi-digit numbers
                curr = curr * 10 + (c as i32 - '0' as i32);
            } else if c == '+' || c == '-' {
                // store what we calculated so far
                output += curr * sign;
                // reset current sum
                curr = 0;
                // set sign
                sign = if c == '-' { -1 } else { 1 };
            } else if c == '(' {
                // store current output and reset
                stack.push(output);
                output = 0;
                // store current sign and reset
                stack.push(sign);
                sign = 1;
            } else if c == ')' {
                // add current value
                output += curr * sign;
                if let [Some(last_sign), Some(last_sum)] = [stack.pop(), stack.pop()] {
                    // multiply by last stored sign
                    output *= last_sign;
                    // add to last stored sum
                    output += last_sum;
                }
                // reset current sum
                curr = 0;
            }
        }

        return output + (curr * sign);
    }
}