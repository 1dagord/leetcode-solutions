/*
    [EASY]
    104. Maximum Depth of Binary Tree

    Concepts:
    - binary tree
    - breadth-first search

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 3.42 MB   [Beats 11.39%]
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
    pub fn max_depth(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut depth_count: i32 = 0;

        if let Some(node) = root {
            let mut queue: VecDeque<Rc<RefCell<TreeNode>>> = VecDeque::from([node]);
            let mut n: usize;
            let mut nd: Rc<RefCell<TreeNode>>;

            while !queue.is_empty() {
                n = queue.len();
                depth_count += 1;

                for _ in 0..n {
                    if let Some(nd) = queue.pop_front() {
                        if let Some(l) = nd.borrow().left.as_ref() {
                            queue.push_back(Rc::clone(l));
                        }
                        if let Some(r) = nd.borrow().right.as_ref() {
                            queue.push_back(Rc::clone(r));
                        }
                    }
                }
            }
        }

        return depth_count;
    }
}
