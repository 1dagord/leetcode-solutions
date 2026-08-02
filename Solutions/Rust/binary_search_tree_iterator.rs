/*
    [MEDIUM]
    173. Binary Search Tree Iterator

    Concepts:
    - binary search tree
    - depth-first search

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 5.28 MB   [Beats 95.45%]
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
use std::rc::Rc;
use std::cell::RefCell;

struct BSTIterator {
    curr: Option<usize>,
    n: usize,
    iot: Vec<i32>
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl BSTIterator {

    fn new(root: Option<Rc<RefCell<TreeNode>>>) -> Self {
        let mut iot = Vec::new();

        fn dfs(curr: Option<Rc<RefCell<TreeNode>>>, iot: &mut Vec<i32>) {
            if let Some(node) = &curr {
                let c = node.borrow();
                dfs(c.left.clone(), iot);
                iot.push(c.val);
                dfs(c.right.clone(), iot);
            }
        }

        dfs(root, &mut iot);

        return BSTIterator {
            curr: None,
            iot: iot.clone(),
            n: iot.len()
        }
    }
    
    fn next(&mut self) -> i32 {
        if let Some(curr) = self.curr.as_mut() {
            *curr += 1;
            return self.iot[*curr];
        }

        self.curr = Some(0);
        return self.iot[0];
    }
    
    fn has_next(&self) -> bool {
        if let Some(curr) = self.curr {
            return if curr + 1 < self.n { true } else { false };
        }
        return if self.iot[0] != -1 { true } else { false };
    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * let obj = BSTIterator::new(root);
 * let ret_1: i32 = obj.next();
 * let ret_2: bool = obj.has_next();
 */
