/*
    [EASY]
    101. Symmetric Tree

    Concepts:
    - binary tree
    - breadth-first search

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.14 MB   [Beats 89.87%]
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
    pub fn is_symmetric(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        fn dfs(node1: Option<Rc<RefCell<TreeNode>>>, node2: Option<Rc<RefCell<TreeNode>>>) -> bool {
            return match [node1, node2] {
                [Some(n1), Some(n2)] => {
                    let [a, b] = [n1.borrow(), n2.borrow()];
                    return (a.val == b.val
                        && dfs(a.left.clone(), b.right.clone())
                        && dfs(a.right.clone(), b.left.clone()));
                }
                [None, None] => {
                    return true;
                }
                [Some(n1), None] => {
                    return false;
                }
                [None, Some(n2)] => {
                    return false;
                }
            };
        }

        if let Some(curr) = &root {
            let c = curr.borrow();
            return dfs(c.left.clone(), c.right.clone());
        }

        return false;
    }
}
