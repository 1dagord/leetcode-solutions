/*
    [HARD]
    124. Binary Tree Maximum Path Sum

    Concepts:
    - binary tree
    - depth-first search

    Stats:
        Runtime | 1 ms      [Beats 30.95%]
        Memory  | 4.39 MB   [Beats 61.90%]
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
use std::cmp::max;
use std::rc::Rc;

impl Solution {
    pub fn max_path_sum(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut max_path_sum = i32::MIN;

        fn traverse(curr: Option<Rc<RefCell<TreeNode>>>, path_sum: &mut i32) -> i32 {
            if let Some(node) = &curr {
                let c = node.borrow();
                let left = max(0, traverse(c.left.clone(), path_sum));
                let right = max(0, traverse(c.right.clone(), path_sum));

                *path_sum = max(*path_sum, left + right + c.val);

                return max(left, right) + c.val;
            }

            return 0;
        }

        traverse(root, &mut max_path_sum);
        return max_path_sum;
    }
}
