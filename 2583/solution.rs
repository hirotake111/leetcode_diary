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
        let mut queue: VecDeque<Rc<RefCell<TreeNode>>> = VecDeque::new();
        let mut heap: BinaryHeap<Reverse<i64>> = BinaryHeap::new();
        let k = k as usize;

        if let Some(node) = root {
            queue.push_back(Rc::clone(&node));
        } else {
            return -1;
        }

        let mut node_count = queue.len();
        let mut total: i64 = 0;
        while let Some(node) = queue.pop_front() {
            node_count -= 1;
            let node = node.borrow();
            total += node.val as i64;
            if let Some(node) = &node.left {
                queue.push_back(Rc::clone(node));
            }
            if let Some(node) = &node.right {
                queue.push_back(Rc::clone(node));
            }
            if node_count == 0 {
                heap.push(Reverse(total));
                total = 0;
                node_count = queue.len();
                if k < heap.len() {
                    heap.pop();
                }
            }
        }

        if heap.len() == k {
            heap.pop().unwrap().0
        } else {
            -1
        }
    }
}
