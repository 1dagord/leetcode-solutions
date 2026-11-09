/*
    [MEDIUM]
    530. Minimum Absolute Difference in BST

    Concepts:
    - binary search tree
    - depth-first search

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 3.09 MB   [Beats 63.16%]
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
use std::cmp::min;
use std::rc::Rc;

impl Solution {
    pub fn get_minimum_difference(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut iot: Vec<i32> = Vec::new();
        let mut min_diff: i32 = i32::MAX;

        fn dfs(curr: Option<Rc<RefCell<TreeNode>>>, iot: &mut Vec<i32>) {
            if let Some(node) = curr {
                let nd = node.borrow();

                dfs(nd.left.clone(), iot);
                iot.push(nd.val);
                dfs(nd.right.clone(), iot);
            }
        }

        dfs(root.clone(), &mut iot);

        for window in iot.windows(2) {
            if let [l, r] = window {
                min_diff = min(min_diff, r - l);
            }
        }

        return min_diff;
    }
}
