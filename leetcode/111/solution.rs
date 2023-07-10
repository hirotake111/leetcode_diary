/**
 * https://leetcode.com/problems/minimum-depth-of-binary-tree/
 * 111. Minimum Depth of Binary Tree
 * Given a binary tree, find its minimum depth.
 * The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
 * Note: A leaf is a node with no children.
 */
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
struct Solution {}

impl Solution {
    pub fn min_depth(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut queue: VecDeque<Rc<RefCell<TreeNode>>> = VecDeque::new();
        if let Some(node) = root {
            queue.push_back(Rc::clone(&node));
        } else {
            return 0;
        }

        let mut depth = 1;
        let mut counts = 1;
        while let Some(node) = queue.pop_front() {
            let node = node.borrow();
            if node.left.is_none() && node.right.is_none() {
                // Found a leaf node
                break;
            }
            if let Some(left) = &node.left {
                queue.push_back(Rc::clone(&left));
            }
            if let Some(right) = &node.right {
                queue.push_back(Rc::clone(&right));
            }
            counts -= 1;
            if counts == 0 {
                depth += 1;
                counts = queue.len();
            }
        }

        depth
    }
}
