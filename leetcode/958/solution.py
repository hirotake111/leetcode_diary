"""
https://leetcode.com/problems/check-completeness-of-a-binary-tree/
958. Check Completeness of a Binary Tree
Given the root of a binary tree, determine if it is a complete binary tree.

In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
"""
from typing import Optional, Deque
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        """BFS approach"""
        # Push nodes to queue until we see None item in it
        q: Deque[Optional[TreeNode]] = deque()
        while root:
            q.append(root.left)
            q.append(root.right)
            root = q.popleft()

        # There all must be None in the queue
        return not any(q)
