/*
    [MEDIUM]
    114. Flatten Binary Tree to Linked List

    Concepts:
    - binary tree
    - linked list
    - depth-first search

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.29 MB   [Beats 75.00%]
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
    pub fn flatten(root: &mut Option<Rc<RefCell<TreeNode>>>) {
        if !root.is_some() {
            return;
        }
        let mut prot: Vec<Rc<RefCell<TreeNode>>> = Vec::new();

        fn dfs(curr: &Option<Rc<RefCell<TreeNode>>>, prot: &mut Vec<Rc<RefCell<TreeNode>>>) {
            if let Some(node) = &curr {
                prot.push(Rc::clone(node));
                dfs(&node.borrow().left, prot);
                dfs(&node.borrow().right, prot);
            }
        }

        dfs(root, &mut prot);

        for i in 0..prot.len() - 1 {
            prot[i].borrow_mut().left = None;
            prot[i].borrow_mut().right = Some(Rc::clone(&prot[i + 1]));
        }
    }
}
