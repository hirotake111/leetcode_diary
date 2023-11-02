use std::cell::RefCell;
/**
 * https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/
 * 2265. Count Nodes Equal to Average of Subtree
 */
use std::rc::Rc;
impl Solution {
    pub fn average_of_subtree(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut count = 0;
        dfs(root, &mut count);
        count
    }
}

fn dfs(node: Option<Rc<RefCell<TreeNode>>>, mut count: &mut i32) -> (i32, i32) {
    match node {
        None => (0, 0),
        Some(node) => {
            let node = node.borrow();
            let left = dfs(node.left.clone(), &mut count);
            let right = dfs(node.right.clone(), &mut count);
            let total = left.0 + right.0 + node.val;
            let num_nodes = left.1 + right.1 + 1;
            if total / num_nodes == node.val {
                *count += 1;
            }

            (total, num_nodes)
        }
    }
}
