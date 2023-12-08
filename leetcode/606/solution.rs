use std::cell::RefCell;
/**
 * https://leetcode.com/problems/construct-string-from-binary-tree/
 * 606. Construct String from Binary Tree
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
    pub fn tree2str(root: Option<Rc<RefCell<TreeNode>>>) -> String {
        fn dfs(node: Rc<RefCell<TreeNode>>) -> String {
            let node = node.borrow();
            match (node.left.clone(), node.right.clone()) {
                (Some(l), Some(r)) => format!("{}({})({})", node.val, dfs(l), dfs(r)),
                (Some(l), None) => format!("{}({})", node.val, dfs(l)),
                (None, Some(r)) => format!("{}()({})", node.val, dfs(r)),
                _ => node.val.to_string(),
            }
        }

        match root {
            Some(node) => dfs(node),
            None => String::new(),
        }
    }
}
