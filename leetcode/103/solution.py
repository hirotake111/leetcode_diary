"""
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
103. Binary Tree Zigzag Level Order Traversal
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).
"""
from typing import List, Optional, Deque, Tuple
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans: List[List[int]] = []
        q = [root]

        while q:
            d = -1 if len(ans) % 2 == 1 else 1
            ans.append([n.val for n in q][::d])
            q = [n for node in q for n in (node.left, node.right) if n]
        return ans
