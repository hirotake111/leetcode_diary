"""
124. Binary Tree Maximum Path Sum
https://leetcode.com/problems/binary-tree-maximum-path-sum/
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    answer: int

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0

            # Get the maximum value of left node and right node
            # But if the value is less than 0, use 0.
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            # Concatenate left, right, and the current value and let's call it path
            path = left + right + node.val
            # If path is greater than the current one, update it
            self.answer = max(self.answer, path)
            # Compare left and right nodes and return greater one, adding node.val
            return max(left, right) + node.val

        # Initialize self.asnwer
        self.answer = -1001
        dfs(root)

        return self.answer
