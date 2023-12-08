"""
https://leetcode.com/problems/construct-string-from-binary-tree/
606. Construct String from Binary Tree
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""
        if root.left and root.right:
            return (
                f"{root.val}({self.tree2str(root.left)})({self.tree2str(root.right)})"
            )
        if root.left:
            return f"{root.val}({self.tree2str(root.left)})"
        if root.right:
            return f"{root.val}()({self.tree2str(root.right)})"
        return f"{root.val}"
