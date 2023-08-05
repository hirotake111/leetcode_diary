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
use std::rc::Rc;
impl Solution {
    pub fn generate_trees(n: i32) -> Vec<Option<Rc<RefCell<TreeNode>>>> {
        create_nodes(1, n as usize)
    }
}

fn create_nodes(begin: usize, end: usize) -> Vec<Option<Rc<RefCell<TreeNode>>>> {
    if begin > end {
        return vec![None];
    }

    let mut nodes = vec![];
    for i in begin..=end {
        let left_nodes = create_nodes(begin, i - 1);
        let right_nodes = create_nodes(i + 1, end);
        for left in &left_nodes {
            for right in &right_nodes {
                let mut node = TreeNode::new(i as i32);
                node.left = left.clone();
                node.right = right.clone();
                nodes.push(Some(Rc::new(RefCell::new(node))));
            }
        }
    }
    nodes
}
