/*
    [MEDIUM]
    86. Partition List

    Concepts:
    - linked list

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.10  MB  [Beats 50.00%]
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
    pub fn partition(mut head: Option<Box<ListNode>>, x: i32) -> Option<Box<ListNode>> {
        let mut lt = Vec::new();
        let mut gte = Vec::new();

        let mut curr = head.as_ref();
        while let Some(node) = curr {
            if node.val < x {
                lt.push(node.val);
            } else {
                gte.push(node.val);
            }
            curr = curr.and_then(|nd| nd.next.as_ref());
        }

        lt.extend(gte);

        let mut curr = head.as_mut();
        let mut idx = 0;
        while let Some(ref mut node) = curr {
            node.val = lt[idx];
            idx += 1;
            curr = curr.and_then(|nd| nd.next.as_mut());
        }

        return head;
    }
}
