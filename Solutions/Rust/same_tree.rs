/*
    [EASY]
    100. Same Tree

    Concepts:
    - binary tree
    - breadth-first search

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.08 MB   [Beats 100%]
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
use std::collections::VecDeque;

impl Solution {
    pub fn is_same_tree(
        p: Option<Rc<RefCell<TreeNode>>>,
        q: Option<Rc<RefCell<TreeNode>>>
    ) -> bool {
        fn bfs(
            root1: Option<Rc<RefCell<TreeNode>>>,
            root2: Option<Rc<RefCell<TreeNode>>>
        ) -> bool {
            let mut queue1: VecDeque<Option<Rc<RefCell<TreeNode>>>>
                = VecDeque::from([root1]);
            let mut queue2: VecDeque<Option<Rc<RefCell<TreeNode>>>>
                = VecDeque::from([root2]);
            let [mut n1, mut n2]: [usize; 2];
            let [mut curr1, mut curr2]: [Option<Rc<RefCell<TreeNode>>>; 2];

            while !queue1.is_empty() && !queue2.is_empty() {
                n1 = queue1.len();
                n2 = queue2.len();

                if n1 != n2 { return false; }

                for _ in 0..n1 {
                    if
                        let Some(curr1) = queue1.pop_front()
                        && let Some(curr2) = queue2.pop_front()
                    {
                        if
                            (curr1.is_some() && !curr2.is_some())
                            || (curr2.is_some() && !curr1.is_some())
                        {
                            return false;
                        }
                        if let Some(c1) = &curr1 && let Some(c2) = &curr2 {
                            if c1.borrow().val != c2.borrow().val { return false; }
                        }

                        for
                            (curr, queue)
                            in [(&curr1, &mut queue1), (&curr2, &mut queue2)]
                        {
                            if let Some(c) = curr {
                                queue.push_back(c.borrow().left.clone());
                                queue.push_back(c.borrow().right.clone());
                            }
                        }
                    }
                }
            }

            return true;
        }

        return bfs(p, q);
    }
}
