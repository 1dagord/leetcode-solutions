/*
    [MEDIUM]
    199. Binary Tree Right Side View

    Concepts:
    - binary tree
    - breadth-first search

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.12 MB   [Beats 69.74%]
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
    pub fn right_side_view(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        let mut levels: Vec<i32> = Vec::new();
        let mut queue: VecDeque<Option<Rc<RefCell<TreeNode>>>> = VecDeque::from([root]);
        let mut n = 0;

        while !queue.is_empty() {
            n = queue.len();

            for i in 0..n {
                if let Some(Some(node)) = queue.pop_front() {
                    let curr = node.borrow();
                    if curr.left.is_some() {
                        queue.push_back(curr.left.clone());
                    }
                    if curr.right.is_some() {
                        queue.push_back(curr.right.clone());
                    }

                    if i == n - 1 {
                        levels.push(curr.val);
                    }
                }
            }
        }

        return levels;
    }
}
