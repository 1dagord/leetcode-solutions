/*
    [MEDIUM]
    61. Rotate List

    Concepts:
    - linked list
    - two pointers

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.14 MB   [Beats 61.32%]
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
    pub fn rotate_right(head: Option<Box<ListNode>>, k: i32) -> Option<Box<ListNode>> {
        // get length of list
        let mut length = 0;
        let mut curr = head.clone();
        while curr.is_some() {
            length += 1;
            curr = curr.and_then(|node| node.next);
        }

        if k == 0 || length == 0 { return head; }

        let mut new_head = head.clone();
        let mut old_tail = Some(Box::new(ListNode{
            val: -1,
            next: new_head.clone()
        }));
        let mut idx = length - (k % length);

        let mut curr = old_tail.clone();
        let mut old_head = curr.as_mut();

        // get head of rotated list
        while idx != 0 && new_head.is_some() {
            old_tail = old_tail.and_then(|node| node.next);
            old_head = old_head.and_then(|node| node.next.as_mut());
            new_head = new_head.and_then(|node| node.next);
            idx -= 1;
        }

        if !new_head.is_some() { return head; }

        // splice lists together
        let mut new_tail = new_head.as_mut();
        while
            let Some(nt) = new_tail.as_ref()
            && let Some(ntn) = nt.next.as_ref()
        {
            new_tail = new_tail.and_then(|node| node.next.as_mut());
        }

        old_head.unwrap().next = None;
        new_tail.unwrap().next = curr.unwrap().next;
        old_tail.unwrap().next = None;

        return new_head;
    }
}
