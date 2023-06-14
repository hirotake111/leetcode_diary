"""
https://leetcode.com/problems/minimum-absolute-difference-in-bst/
530. Minimum Absolute Difference in BST

Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        arr = []

        def dfs(node: TreeNode):
            if node.left:
                dfs(node.left)
            arr.append(node.val)
            if node.right:
                dfs(node.right)

        if root is None:
            raise ValueError("No way!")

        dfs(root)
        min_value = 100001
        for i in range(len(arr) - 1):
            min_value = min(min_value, abs(arr[i] - arr[i + 1]))
        return min_value
