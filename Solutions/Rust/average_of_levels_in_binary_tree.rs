/*
    [EASY]
    637. Average of Levels in Binary Tree

    Concepts:
    - binary tree
    - breadth-first search

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.98 MB   [Beats 83.33%]
*/
// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
//
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::cell::RefCell;
use std::collections::VecDeque;
use std::rc::Rc;

impl Solution {
    pub fn average_of_levels(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<f64> {
        let mut averages: Vec<f64> = Vec::new();

        let mut queue: VecDeque<Option<Rc<RefCell<TreeNode>>>> = VecDeque::from([root]);
        let [mut level_len, mut level_sum]: [f64; 2] = [0.0, 0.0];

        while !queue.is_empty() {
            level_len = queue.len() as f64;
            level_sum = 0.0;

            for _ in 0..level_len as usize {
                if let Some(Some(node)) = queue.pop_front() {
                    let curr = node.borrow();
                    level_sum += curr.val as f64;

                    if curr.left.is_some() {
                        queue.push_back(curr.left.clone());
                    }
                    if curr.right.is_some() {
                        queue.push_back(curr.right.clone());
                    }
                }
            }

            averages.push(level_sum / level_len);
        }

        return averages;
    }
}
