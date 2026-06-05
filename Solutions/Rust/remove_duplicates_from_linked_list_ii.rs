/*
    [MEDIUM]
    82. Remove Duplicates from Sorted List II

    Concepts:
    - linked list

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.18 MB   [Beats 60.87%]
*/
use std::collections::BTreeMap;

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
    pub fn delete_duplicates(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut counter: BTreeMap<i32, i32> = BTreeMap::new();
        let mut curr = head;

        while curr.is_some() {
            if let Some(node) = &curr {
                counter.entry(node.val).and_modify(|v| *v += 1).or_insert(1);
            }
            curr = curr.and_then(|node| node.next);
        }

        let mut dummy = Some(Box::new(ListNode::new(-1)));
        let mut new_head = dummy.as_mut();

        for (val, count) in counter {
            if count == 1 {
                if let Some(nd) = &mut new_head {
                    nd.next = Some(Box::new(ListNode::new(val)));
                }
                new_head = new_head.and_then(|node| node.next.as_mut());
            }
        }

        return dummy.unwrap().next;
    }
}
