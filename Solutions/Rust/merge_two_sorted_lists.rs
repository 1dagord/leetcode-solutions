/*
    [EASY]
    21. Merge Two Sorted Lists

    Concepts:
    - linked list

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.20 MB   [Beats 54.86%]
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
    pub fn merge_two_lists(mut l1: Option<Box<ListNode>>, mut l2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut head: Box<ListNode> = Box::new(ListNode::new(-1));
        let mut res: &mut Box<ListNode> = &mut head;

        while l1.is_some() && l2.is_some() {
            if let [Some(a), Some(b)] = [l1.as_ref(), l2.as_ref()] {
                if a.val <= b.val {
                    res.next = l1.clone();
                    l1 = l1.and_then(|node| node.next);
                } else {
                    res.next = l2.clone();
                    l2 = l2.and_then(|node| node.next);
                }
            }

            res = res.next.as_mut().unwrap();
        }

        if l1.is_some() {
            res.next = l1.clone();
        } else if l2.is_some() {
            res.next = l2.clone();
        }

        return head.next;
    }
}