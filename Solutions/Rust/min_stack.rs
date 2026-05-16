/*
    [MEDIUM]
    155. Min Stack

    Concepts:
    - stack
    - design

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 6.00 MB   [Beats 63.77%]
*/
use std::cmp::min;

struct MinStack {
    stack: Vec<[i32; 2]>
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MinStack {

    fn new() -> Self {
        return MinStack {
            stack: Vec::new()
        };
    }
    
    fn push(&mut self, val: i32) {
        if let Some(stack_last) = self.stack.last() {
            self.stack.push([val, min(val, stack_last[1])]);
        } else {
            self.stack.push([val, val]);
        }
    }
    
    fn pop(&mut self) {
        self.stack.pop();
    }
    
    fn top(&mut self) -> i32 {
        return match self.stack.last() {
            Some(stack_last) => stack_last[0],
            None => 0
        }
    }
    
    fn get_min(&mut self) -> i32 {
        return match self.stack.last() {
            Some(stack_last) => stack_last[1],
            None => 0
        }
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * let obj = MinStack::new();
 * obj.push(val);
 * obj.pop();
 * let ret_3: i32 = obj.top();
 * let ret_4: i32 = obj.get_min();
 */