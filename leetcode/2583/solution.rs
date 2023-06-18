// Definition for a binary tree node.
#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}
impl TreeNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        TreeNode {
            val,
            left: None,
            right: None,
        }
    }
}

struct Solution {}

use std::cell::RefCell;
use std::cmp::Reverse;
use std::collections::{BinaryHeap, VecDeque};
use std::rc::Rc;

impl Solution {
    pub fn kth_largest_level_sum(root: Option<Rc<RefCell<TreeNode>>>, k: i32) -> i64 {
        // Define queue and priority queue (heap)
        let mut queue: VecDeque<Rc<RefCell<TreeNode>>> = VecDeque::new();
        let mut heap: BinaryHeap<Reverse<i64>> = BinaryHeap::new();
        let k = k as usize;

        // Push the root into the queue
        if let Some(node) = root {
            queue.push_back(Rc::clone(&node));
        } else {
            return -1;
        }

        // Get the level sum for each level
        let mut total: i64 = 0;
        let mut node_counts = 1;
        while let Some(node) = queue.pop_front() {
            node_counts -= 1;
            let node = node.borrow();
            total += node.val as i64;
            // Add child node if exists to the queue
            if let Some(child) = &node.left {
                queue.push_back(Rc::clone(child));
            }
            if let Some(child) = &node.right {
                queue.push_back(Rc::clone(child));
            }
            // Check to see if the current node is the last one in the level
            if node_counts == 0 {
                // Push the total into the heap
                heap.push(Reverse(total));
                // reset total
                total = 0;
                // re-initialize node counts
                node_counts = queue.len();
                // if needed remove one item from the heap
                if heap.len() > k {
                    heap.pop();
                }
            }
        }

        // If the length of the queue is less than k, return -1
        if heap.len() == k {
            heap.pop().unwrap().0
        } else {
            -1
        }
    }
}
