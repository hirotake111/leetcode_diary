"""
https://leetcode.com/problems/symmetric-tree/
101. Symmetric Tree
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(a, b):
            if a == b == None:
                return True

            if a is None or b is None:
                return False

            if a.val != b.val:
                return False

            # At this pint both a and b exist and have the same value
            # Move on to their child nodes
            return dfs(a.left, b.right) and dfs(a.right, b.left)

        return dfs(root, root)
