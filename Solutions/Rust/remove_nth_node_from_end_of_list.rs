/*
    [MEDIUM]
    19. Remove Nth Node From End of List

    Concepts:
    - linked list
    - two pointers

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.16 MB   [Beats 60.87%]
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
    pub fn remove_nth_from_end(head: Option<Box<ListNode>>, mut n: i32) -> Option<Box<ListNode>> {
        let mut dummy = Box::new(ListNode::new(-1));
        dummy.next = head.clone();
        let mut left: Option<&mut Box<ListNode>> = Some(&mut dummy);
        let mut right: Option<Box<ListNode>> = head.clone();

        // iterate n nodes into list
        while right.is_some() && n != 0 {
            right = right.and_then(|node| node.next);
            n -= 1
        }

        // put prev into position
        while right.is_some() {
            left = left.and_then(|node| node.next.as_mut());
            right = right.and_then(|node| node.next);
        }

        // splice out node
        left.unwrap().next = left
            .as_ref()
            .and_then(|node| node.next.as_ref())
            .and_then(|node| node.next.as_ref())
            .cloned();
        return dummy.next;   
    }
}
