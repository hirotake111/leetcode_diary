"""
https://leetcode.com/problems/binary-tree-preorder-traversal/
144. Binary Tree Preorder Traversal

---
Algorithm Preorder(tree)

Visit the root.
Traverse the left subtree, i.e., call Preorder(left->subtree)
Traverse the right subtree, i.e., call Preorder(right->subtree) 
"""
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer: List[int] = []

        def dfs(node: TreeNode) -> None:
            # First, append the value of current node
            answer.append(node.val)
            # If node has a left node, recursively append value of the left node
            if node.left:
                dfs(node.left)
            # If node has a right node, recursively append value of the right node
            if node.right:
                dfs(node.right)

        # Edge case: return [] if root is not a node
        if root is None:
            return []
        dfs(root)
        return answer
