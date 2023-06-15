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

use std::cell::RefCell;
use std::collections::VecDeque;
use std::rc::Rc;

impl Solution {
    pub fn max_level_sum(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut smallest_level = 1;
        let mut max_total = i32::MIN;
        let mut queue: VecDeque<Rc<RefCell<TreeNode>>> = VecDeque::new();
        queue.push_back(root.unwrap());

        let mut num_nodes = queue.len();
        let mut current_level = 1;
        let mut current_total = 0;
        while let Some(node) = queue.pop_front() {
            num_nodes -= 1;
            let node = node.borrow();
            current_total += node.val;
            if let Some(node) = &node.left {
                queue.push_back(Rc::clone(node));
            }
            if let Some(node) = &node.right {
                queue.push_back(Rc::clone(node));
            }
            if num_nodes == 0 {
                // End of level
                if max_total < current_total {
                    max_total = current_total;
                    smallest_level = current_level;
                }
                num_nodes = queue.len();
                current_level += 1;
                current_total = 0;
            }
        }

        smallest_level
    }
}
