"""
https://leetcode.com/problems/same-tree/
100. Same Tree
Companies
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both doesn't exist, return True
        if p is None and q is None:
            return True

        if p and q:
            # If both nodes exist but values are different,
            # return False
            if p.val != q.val:
                return False
            # Else, search left and right node
            left = self.isSameTree(p.left, q.left)
            right = self.isSameTree(p.right, q.right)
            return left and right

        # If one exists and other doesn't, return False
        return False
