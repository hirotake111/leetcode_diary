/**
 * https://leetcode.com/problems/partition-list/
 * 86. Partition List
 */

// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }
}

use std::cmp::Ordering;
impl Solution {
    pub fn partition(mut head: Option<Box<ListNode>>, x: i32) -> Option<Box<ListNode>> {
        let mut small = ListNode::new(-1);
        let mut large = ListNode::new(-1);
        // Borrow a mutable reference from small and large.
        // And in the subsequent while loop we basically handle small_tail and large tail
        // small and large are respectively used in the final phase to concatenate each other
        let mut small_tail = &mut small;
        let mut large_tail = &mut large;

        while let Some(mut node) = head {
            // take() takes the value out of node.next, leaving ga None in it
            head = node.next.take();
            if node.val < x {
                small_tail.next = Some(node);
                // as_mut() converts from &mut Option<Box<ListNode>> to Option<&mut Box<ListNode>>
                // so that small should be &mut Box<ListNode>
                small_tail = small_tail.next.as_mut().unwrap();
            } else {
                large_tail.next = Some(node);
                large_tail = large_tail.next.as_mut().unwrap();
            }
        }
        small_tail.next = large.next.take();
        small.next
    }
}
