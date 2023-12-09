use std::cell::RefCell;
/**
 * https://leetcode.com/problems/binary-tree-inorder-traversal/
 * 94. Binary Tree Inorder Traversal
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
    pub fn inorder_traversal(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        fn dfs(node: Rc<RefCell<TreeNode>>) -> Vec<i32> {
            let mut v = vec![];
            let node = node.borrow();
            if let Some(left) = &node.left {
                v.append(&mut dfs(left.clone()));
            }
            v.push(node.val);
            if let Some(right) = &node.right {
                v.append(&mut dfs(right.clone()));
            }
            v
        }

        if let Some(node) = root {
            dfs(node)
        } else {
            vec![]
        }
    }
}
