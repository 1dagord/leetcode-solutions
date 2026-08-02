/*
    [MEDIUM]
    129. Sum Root to Leaf Numbers

    Concepts:
    - binary tree
    - depth-first search

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.21 MB   [Beats 21.43%]
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
    pub fn sum_numbers(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut rtl_sum = 0;
        fn convert(l: &mut Vec<i32>) -> i32 {
            return l
                .iter()
                .rev()
                .enumerate()
                .fold(0, |acc, (i, v)| acc + (v * (10_i32.pow(i as u32))));
        };

        fn dfs(curr: Option<Rc<RefCell<TreeNode>>>, path: &mut Vec<i32>, sum: &mut i32) {
            if let Some(node) = &curr {
                let c = node.borrow();

                if let Some(left) = &c.left {
                    path.push(left.borrow().val);
                    dfs(Some(Rc::clone(left)), path, sum);
                    path.pop();
                }
                if let Some(right) = &c.right {
                    path.push(right.borrow().val);
                    dfs(Some(Rc::clone(right)), path, sum);
                    path.pop();
                }

                if !c.left.is_some() && !c.right.is_some() {
                    *sum += convert(path);
                }
            }
        }

        if let Some(r) = &root {
            let mut path: Vec<i32> = Vec::from([r.borrow().val]);
            dfs(Some(Rc::clone(r)), &mut path, &mut rtl_sum);
        }

        return rtl_sum;
    }
}
