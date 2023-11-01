use std::cell::RefCell;
/**
 * https://leetcode.com/problems/find-mode-in-binary-search-tree/
 * 501. Find Mode in Binary Search Tree
 */
// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
//
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::rc::Rc;
impl Solution {
    pub fn find_mode(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        let mut freq = std::collections::HashMap::new();
        let mut queue = std::collections::VecDeque::new();

        if let Some(node) = root {
            queue.push_back(node);
        }

        while let Some(node) = queue.pop_front() {
            let node = node.borrow();
            *freq.entry(node.val).or_insert(0) += 1;
            if let Some(left) = &node.left {
                queue.push_back(left.clone());
            }
            if let Some(right) = &node.right {
                queue.push_back(right.clone());
            }
        }

        let max = *freq.values().max().unwrap_or(&0);
        freq.iter()
            .filter(|(_, &v)| v == max)
            .map(|(&k, _)| k)
            .collect()
    }
}
