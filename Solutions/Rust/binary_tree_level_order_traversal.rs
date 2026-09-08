/*
    [MEDIUM]
    102. Binary Tree Level Order Traversal

    Concepts:
    - binary tree
    - breadth-first search

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.58 MB  [Beats 28.57%]
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
    pub fn level_order(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Vec<i32>> {
        if !root.is_some() {
            return Vec::new();
        }
        let mut levels: Vec<Vec<i32>> = Vec::new();

        let mut queue: VecDeque<Option<Rc<RefCell<TreeNode>>>> = VecDeque::from([root]);
        let mut n = 0;

        while !queue.is_empty() {
            n = queue.len();
            let mut level: Vec<i32> = Vec::new();

            for _ in 0..n {
                if let Some(Some(node)) = queue.pop_front() {
                    let curr = node.borrow();
                    level.push(curr.val);

                    if curr.left.is_some() {
                        queue.push_back(curr.left.clone());
                    }
                    if curr.right.is_some() {
                        queue.push_back(curr.right.clone());
                    }
                }
            }

            levels.push(level);
        }

        return levels;
    }
}
