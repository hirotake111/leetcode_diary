"""
https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/
1372. Longest ZigZag Path in a Binary Tree

You are given the root of a binary tree.

A ZigZag path for a binary tree is defined as follow:

Choose any node in the binary tree and a direction (right or left).
If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
Change the direction from right to left or from left to right.
Repeat the second and third steps until you can't move in the tree.
Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest ZigZag path contained in that tree.
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        longest = [0]

        def dfs(node: TreeNode, edges: int, right: bool):
            if node.left:
                dfs(node.left, edges + 1 if right else 1, False)
            if node.right:
                dfs(node.right, 1 if right else edges + 1, True)

            # Update the answer
            longest[0] = max(longest[0], edges)

        if root is None:
            return 0

        if root.left:
            dfs(root.left, 1, False)
        if root.right:
            dfs(root.right, 1, True)

        return longest[0]
