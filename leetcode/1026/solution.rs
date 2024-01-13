use std::cell::RefCell;
/**
 * 1026. Maximum Difference Between Node and Ancestor
 * https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
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
    pub fn max_ancestor_diff(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        if let Some(node) = root {
            dfs(node, i32::MAX, i32::MIN)
        } else {
            panic!("no way");
        }
    }
}

fn dfs(node: Rc<RefCell<TreeNode>>, min: i32, max: i32) -> i32 {
    let node = node.borrow();
    // maintain min and max
    let min = min.min(node.val);
    let max = max.max(node.val);
    let mut diff = max - min;
    // update diff based on child nodes
    match (node.left.clone(), node.right.clone()) {
        (None, None) => diff,
        (Some(left), None) => diff.max(dfs(left, min, max)),
        (None, Some(right)) => diff.max(dfs(right, min, max)),
        (Some(left), Some(right)) => diff.max(dfs(left, min, max)).max(dfs(right, min, max)),
    }
}
