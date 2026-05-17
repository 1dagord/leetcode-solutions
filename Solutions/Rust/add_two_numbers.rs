/*
    [MEDIUM]
    2. Add Two Numbers

    Concepts:
    - linked list
    - math

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.18 MB   [Beats 96.57%]
*/

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
    pub fn add_two_numbers(mut l1: Option<Box<ListNode>>, mut l2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut res_head: Box<ListNode> = Box::new(ListNode::new(-1));
        let mut res: &mut Box<ListNode> = &mut res_head;
        let [mut carry, mut sum_val]: [i32; 2] = [0, 0];

        while l1.is_some() || l2.is_some() || carry != 0 {
            sum_val = l1.as_ref().map_or(0, |x| x.val)
                + l2.as_ref().map_or(0, |x| x.val)
                + carry;
            carry = if sum_val > 9 { 1 } else { 0 };
            res.next = Some(Box::new(ListNode::new(sum_val % 10)));

            l1 = l1.and_then(|node| node.next);
            l2 = l2.and_then(|node| node.next);
            res = res.next.as_mut().unwrap();
        }

        return res_head.next;
    }
}