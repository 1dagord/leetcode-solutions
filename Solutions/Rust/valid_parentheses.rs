/*
    [EASY]
    20. Valid Parentheses

    Concepts:
    - stack
    - string

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.22 MB   [Beats 30.79%]
*/
use std::collections::HashMap;

impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut stack: Vec<char> = Vec::new();
        let brackets: HashMap<char, char> = HashMap::from([
            ('(', ')'),
            ('[', ']'),
            ('{', '}')
        ]);

        for c in s.chars() {
            // if c is an opening bracket...
            if brackets.contains_key(&c) {
                stack.push(c);
            } else {
                if stack.is_empty() { return false; }

                if let Some(brack) = stack.pop() {
                    if c != brackets[&brack] { return false; }
                }
            }
        }

        return stack.is_empty();
    }
}