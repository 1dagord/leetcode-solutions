/*
    [MEDIUM]
    2130. Maximum Twin Sum of a Linked List

    Concepts:
    - linked list

    Stats:
        Runtime | 14 ms     [Beats 60.71%]
        Memory  | 6.81 MB   [Beats 75.00%]
*/

use std::cmp::max;

// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
//
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }
impl Solution {
    pub fn pair_sum(mut head: Option<Box<ListNode>>) -> i32 {
        let mut vals = Vec::new();
        let mut max_sum = 0;

        while let Some(node) = head.as_mut() {
            vals.push(node.val);
            head = node.next.take();
        }

        let n = vals.len();
        for i in 0..n / 2 {
            max_sum = max(vals[i] + vals[n - 1 - i], max_sum);
        }

        return max_sum;
    }
}
