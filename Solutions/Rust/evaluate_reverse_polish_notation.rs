/*
    [MEDIUM]
    150. Evaluate Reverse Polish Notation

    Concepts:
    - stack
    - math

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.68 MB   [Beats 98.48%]
*/
use std::collections::HashSet;

impl Solution {
    pub fn eval_rpn(tokens: Vec<String>) -> i32 {
        let mut stack: Vec<i32> = Vec::new();
        let ops: HashSet<&str> = HashSet::from(["+", "-", "*", "/"]);

        for c in tokens {
            if ops.contains(c.as_str()) {
                if let [Some(b), Some(a)] = [stack.pop(), stack.pop()] {
                    stack.push(
                        match c.as_str() {
                            "+" => a + b,
                            "-" => a - b,
                            "*" => a * b,
                            _ => a / b
                        }
                    );
                }
            } else {
                stack.push(c.parse::<i32>().unwrap());
            }
        }

        return stack[0];
    }
}