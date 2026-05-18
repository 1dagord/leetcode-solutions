/*
    [MEDIUM]
    92. Reverse Linked List II

    Concepts:
    - linked list

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.57 MB   [Beats 17.24%]
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
    pub fn reverse_between(head: Option<Box<ListNode>>, mut left: i32, mut right: i32) -> Option<Box<ListNode>> {
        /*
            Use LIFO properties of stack to reverse node
            and splice together reversed portion with
            prepended and appended list
        */
        let mut dummy = Some(Box::new(ListNode::new(-1)));
        if let Some(ref mut node) = dummy {
            node.next = head.clone()
        }

        let mut post: Option<Box<ListNode>> = head.clone();
        let mut curr: Option<Box<ListNode>> = dummy.clone();
        let mut prev: Option<Box<ListNode>> = dummy.clone();
        let mut pre: Option<&mut Box<ListNode>> = dummy.as_mut();

        if left == right { return head; }

        // shift in curr and post pointers
        while right - left != 0 {
            curr = curr.and_then(|node| node.next);
            post = post.and_then(|node| node.next);
            right -= 1;
        }

        while left != 0 {
            if left > 1 {
                pre = pre.and_then(|node| node.next.as_mut());
            }

            prev = prev.and_then(|node| node.next);
            curr = curr.and_then(|node| node.next);
            post = post.and_then(|node| node.next);

            left -= 1;
        }

        // add all nodes in between to stack
        let mut middle_nodes = Vec::new();
        while prev != post {
            middle_nodes.push(prev.clone());
            prev = prev.and_then(|node| node.next);
        }

        // pop nodes off stack and appent to list
        if let Some(ref mut p) = pre {
            while !middle_nodes.is_empty() {
                if let Some(node) = middle_nodes.pop() {
                    p.next = node;
                    *p = p.next.as_mut().unwrap();
                }
            }

            if post.is_some() {
                p.next = post;
            } else {
                p.next = None;
            }
        }

        return dummy.and_then(|node| node.next);
    }
}