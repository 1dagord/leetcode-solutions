/*
    [MEDIUM]
    106. Construct Binary Tree from Inorder and Postorder Traversal

    Concepts:
    - binary tree
    - divide and conquer

    Stats:
        Runtime | 2 ms      [Beats 15.79%]
        Memory  | 2.71 MB   [Beats 57.89%]
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
    pub fn build_tree(inorder: Vec<i32>, postorder: Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {
        fn construct(iot: &[i32], pot: &[i32]) -> Option<Rc<RefCell<TreeNode>>> {
            if iot.is_empty() || pot.is_empty() {
                return None;
            }

            let mut root = Rc::new(RefCell::new(TreeNode::new(pot[pot.len() - 1])));

            // index of root in iot
            let idx: usize = iot.iter().position(|&v| v == pot[pot.len() - 1]).unwrap();

            root.borrow_mut().left = construct(&iot[..idx], &pot[..idx]);
            root.borrow_mut().right = construct(&iot[idx + 1..], &pot[idx..pot.len() - 1]);

            return Some(root);
        }

        return construct(inorder.as_slice(), postorder.as_slice());
    }
}
