/*
    [MEDIUM]
    2095. Delete the Middle Node of a Linked List
    
    Concepts:
    - linked list
    - two pointers

    Stats:
        Runtime | 83 ms     [Beats 8.70%]
        Memory  | 14.61 MB  [Beats 8.70%]
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
    pub fn delete_middle(mut head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        if !head.is_some() { return head; }
        if let Some(node) = head.as_mut() {
            if !node.next.is_some() { return node.next.take(); }
        }

        let mut h = head.clone();
        let mut fast = h.clone();
        let mut slow: Option<&mut Box<ListNode>> = None;

        // get node right before middle node
        while let Some(f) = fast.as_mut() && let Some(ff) = f.next.as_mut() {
            fast = ff.next.take();
            if let Some(s) = &slow {
                slow = slow.and_then(|node| node.next.as_mut());
            } else {
                slow = h.as_mut();
            }
        }

        // splice out middle node
        if let Some(s) = slow.as_mut() && let Some(ss) = s.next.as_mut() {
            s.next = ss.next.take();
        }

        return h;
    }
}
