/*
    [EASY]
    226. Invert Binary Tree

    Concepts:
    - binary tree
    - breadth-first search

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.08 MB   [Beats 95.33%]
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
use std::rc::Rc;

impl Solution {
    pub fn invert_tree(mut root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        fn invert(mut c: Option<Rc<RefCell<TreeNode>>>) {
            if let Some(node) = c {
                let mut curr = node.borrow_mut();

                let temp = curr.left.clone();
                curr.left = curr.right.take();
                curr.right = temp;

                if let Some(left) = &curr.left {
                    invert(Some(Rc::clone(left)));
                }
                if let Some(right) = &curr.right {
                    invert(Some(Rc::clone(right)));
                }
            }
        }

        if let Some(r) = &root {
            invert(Some(Rc::clone(r)));
        }
        return root;
    }
}
