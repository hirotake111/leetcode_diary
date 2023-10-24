use std::cell::RefCell;
/**
 * https://leetcode.com/problems/find-largest-value-in-each-tree-row/
 * 515. Find Largest Value in Each Tree Row
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
    pub fn largest_values(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        let mut answer: Vec<i32> = vec![];
        let mut queue = std::collections::VecDeque::new();

        match root {
            Some(node) => queue.push_back((node.clone(), 0)),
            None => return answer,
        }

        while let Some((node, i)) = queue.pop_front() {
            if answer.len() == i {
                answer.push(std::i32::MIN);
            }
            let node = node.borrow();
            answer[i] = answer[i].max(node.val);
            if let Some(left) = node.left.clone() {
                queue.push_back((left, i + 1));
            }
            if let Some(right) = node.right.clone() {
                queue.push_back((right, i + 1));
            }
        }

        answer
    }
}
