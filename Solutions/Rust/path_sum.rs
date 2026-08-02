/*
    [EASY]
    112. Path Sum

    Concepts:
    - depth-first search
    - binary tree

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.72 MB   [Beats 44.00%]
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
    pub fn has_path_sum(root: Option<Rc<RefCell<TreeNode>>>, target: i32) -> bool {
        fn dfs(curr: Option<Rc<RefCell<TreeNode>>>, path_sum: i32, target: i32) -> bool {
            let mut outcome = false;

            if let Some(node) = curr {
                let c = node.borrow();
                if !c.left.is_some() && !c.right.is_some() && path_sum == target {
                    return true;
                }

                if let Some(left) = &c.left {
                    outcome |= dfs(c.left.clone(), path_sum + left.borrow().val, target);
                }
                if let Some(right) = &c.right {
                    outcome |= dfs(c.right.clone(), path_sum + right.borrow().val, target);
                }
            }

            return outcome;
        }

        if let Some(r) = &root {
            return dfs(Some(Rc::clone(r)), r.borrow().val, target);
        }

        return false;
    }
}
