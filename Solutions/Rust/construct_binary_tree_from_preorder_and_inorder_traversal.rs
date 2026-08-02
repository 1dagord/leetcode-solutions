/*
    [MEDIUM]
    105. Construct Binary Tree from Preorder and Inorder Traversal

    Concepts:
    - binary tree
    - divide and conquer

    Stats:
        Runtime | 4 ms      [Beats 22.73%]
        Memory  | 2.82 MB   [Beats 43.18%]
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
    pub fn build_tree(preorder: Vec<i32>, inorder: Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {
        fn construct(prot: &[i32], iot: &[i32]) -> Option<Rc<RefCell<TreeNode>>> {
            if prot.is_empty() || iot.is_empty() {
                return None;
            }

            let mut root = Rc::new(RefCell::new(TreeNode::new(prot[0])));

            // index of root in iot
            let idx: usize = iot.iter().position(|&v| v == prot[0]).unwrap();

            root.borrow_mut().left = construct(&prot[1..idx + 1], &iot[..idx]);
            root.borrow_mut().right = construct(&prot[idx + 1..], &iot[idx + 1..]);

            return Some(root);
        }

        return construct(preorder.as_slice(), inorder.as_slice());
    }
}
